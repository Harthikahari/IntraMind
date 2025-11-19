"""
Unit tests for the ChatBot class.
"""

import pytest
from intramind import ChatBot, Config
from intramind.core.chatbot import ChatResponse


class TestChatBot:
    """Test suite for ChatBot class."""

    def test_chatbot_initialization(self):
        """Test that ChatBot initializes correctly."""
        bot = ChatBot()
        assert bot is not None
        assert bot.config is not None
        assert bot.nlp_engine is not None
        assert bot.conversation_manager is not None

    def test_chatbot_with_custom_config(self):
        """Test ChatBot initialization with custom config."""
        config = Config(app_name="TestBot")
        bot = ChatBot(config)
        assert bot.config.app_name == "TestBot"

    def test_chat_basic_message(self):
        """Test basic chat functionality."""
        bot = ChatBot()
        response = bot.chat("Hello")

        assert isinstance(response, ChatResponse)
        assert response.message is not None
        assert isinstance(response.message, str)
        assert len(response.message) > 0

    def test_chat_with_session(self):
        """Test chat with session management."""
        bot = ChatBot()
        session_id = "test-session-001"

        response1 = bot.chat("Hello", session_id=session_id)
        assert response1.session_id == session_id

        response2 = bot.chat("How are you?", session_id=session_id)
        assert response2.session_id == session_id

    def test_chat_response_attributes(self):
        """Test that ChatResponse has expected attributes."""
        bot = ChatBot()
        response = bot.chat("Test message")

        assert hasattr(response, 'message')
        assert hasattr(response, 'confidence')
        assert hasattr(response, 'intent')
        assert hasattr(response, 'entities')
        assert hasattr(response, 'session_id')
        assert hasattr(response, 'metadata')

    def test_clear_session(self):
        """Test clearing a conversation session."""
        bot = ChatBot()
        session_id = "test-session-002"

        bot.chat("Hello", session_id=session_id)
        result = bot.clear_session(session_id)
        assert result is True

    def test_get_session_history(self):
        """Test retrieving session history."""
        bot = ChatBot()
        session_id = "test-session-003"

        bot.chat("Message 1", session_id=session_id)
        bot.chat("Message 2", session_id=session_id)

        history = bot.get_session_history(session_id)
        assert isinstance(history, list)
        assert len(history) >= 2

    @pytest.mark.asyncio
    async def test_chat_async(self):
        """Test async chat functionality."""
        bot = ChatBot()
        response = await bot.chat_async("Hello async!")

        assert isinstance(response, ChatResponse)
        assert response.message is not None


class TestChatResponse:
    """Test suite for ChatResponse dataclass."""

    def test_chat_response_creation(self):
        """Test creating a ChatResponse object."""
        response = ChatResponse(
            message="Test response",
            confidence=0.95,
            intent="greeting",
            session_id="test-001"
        )

        assert response.message == "Test response"
        assert response.confidence == 0.95
        assert response.intent == "greeting"
        assert response.session_id == "test-001"
