"""
Main ChatBot class for IntraMind.

Handles conversation management, response generation, and integration
with AI models.
"""

import asyncio
from typing import Any, Dict, Optional, List
from dataclasses import dataclass
import logging

from intramind.core.config import Config
from intramind.core.nlp_engine import NLPEngine
from intramind.core.conversation import ConversationManager

logger = logging.getLogger(__name__)


@dataclass
class ChatResponse:
    """
    Response from the chatbot.

    Attributes:
        message: The response text
        confidence: Confidence score (0-1)
        intent: Detected intent
        entities: Extracted entities
        session_id: Session identifier
        metadata: Additional response metadata
    """
    message: str
    confidence: float
    intent: Optional[str] = None
    entities: Optional[Dict[str, Any]] = None
    session_id: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None


class ChatBot:
    """
    Main ChatBot class for conversational AI.

    This class orchestrates the entire conversation flow, from receiving
    user input to generating and returning responses.

    Example:
        >>> from intramind import ChatBot, Config
        >>> config = Config()
        >>> bot = ChatBot(config)
        >>> response = bot.chat("Hello!")
        >>> print(response.message)
    """

    def __init__(self, config: Optional[Config] = None):
        """
        Initialize the ChatBot.

        Args:
            config: Configuration object. If None, uses default config.
        """
        self.config = config or Config()
        self.nlp_engine = NLPEngine(self.config)
        self.conversation_manager = ConversationManager(self.config)
        logger.info(f"ChatBot initialized with provider: {self.config.ai_provider}")

    def chat(self, message: str, session_id: Optional[str] = None,
             context: Optional[Dict[str, Any]] = None) -> ChatResponse:
        """
        Process a user message and return a response.

        Args:
            message: User's input message
            session_id: Optional session identifier for conversation continuity
            context: Optional context dictionary for the conversation

        Returns:
            ChatResponse object containing the bot's response and metadata

        Example:
            >>> response = bot.chat("What can you do?")
            >>> print(response.message)
        """
        try:
            # Process the message through NLP engine
            nlp_result = self.nlp_engine.process(message)

            # Get or create conversation session
            session = self.conversation_manager.get_or_create_session(
                session_id=session_id,
                context=context
            )

            # Add message to conversation history
            session.add_message("user", message)

            # Generate response (placeholder - integrate with actual AI model)
            response_text = self._generate_response(
                message=message,
                nlp_result=nlp_result,
                session=session
            )

            # Add bot response to history
            session.add_message("assistant", response_text)

            return ChatResponse(
                message=response_text,
                confidence=nlp_result.get("confidence", 0.9),
                intent=nlp_result.get("intent"),
                entities=nlp_result.get("entities"),
                session_id=session.session_id,
                metadata={"model": self.config.model_name}
            )

        except Exception as e:
            logger.error(f"Error processing message: {str(e)}")
            return ChatResponse(
                message="I apologize, but I encountered an error processing your message.",
                confidence=0.0,
                metadata={"error": str(e)}
            )

    async def chat_async(self, message: str, session_id: Optional[str] = None,
                        context: Optional[Dict[str, Any]] = None) -> ChatResponse:
        """
        Async version of chat method for high-performance applications.

        Args:
            message: User's input message
            session_id: Optional session identifier
            context: Optional context dictionary

        Returns:
            ChatResponse object
        """
        # Run the synchronous chat method in a thread pool
        return await asyncio.to_thread(self.chat, message, session_id, context)

    def _generate_response(self, message: str, nlp_result: Dict[str, Any],
                          session: Any) -> str:
        """
        Generate a response based on the message and NLP analysis.

        This is a placeholder that should be replaced with actual
        AI model integration (OpenAI GPT-4, Azure OpenAI, etc.)

        Args:
            message: The user's message
            nlp_result: Results from NLP processing
            session: Current conversation session

        Returns:
            Generated response text
        """
        # TODO: Integrate with actual AI model
        # For now, return a placeholder response

        intent = nlp_result.get("intent", "unknown")

        if intent == "greeting":
            return "Hello! How can I assist you today?"
        elif intent == "farewell":
            return "Goodbye! Have a great day!"
        else:
            return (
                "I'm IntraMind, an enterprise-grade AI assistant. "
                "I'm currently in setup mode. Please configure your "
                "OpenAI API key in the .env file to enable "
                "full conversational capabilities."
            )

    def clear_session(self, session_id: str) -> bool:
        """
        Clear a conversation session.

        Args:
            session_id: Session identifier to clear

        Returns:
            True if session was cleared, False otherwise
        """
        return self.conversation_manager.clear_session(session_id)

    def get_session_history(self, session_id: str) -> List[Dict[str, str]]:
        """
        Get the conversation history for a session.

        Args:
            session_id: Session identifier

        Returns:
            List of messages in the session
        """
        session = self.conversation_manager.get_session(session_id)
        return session.get_history() if session else []
