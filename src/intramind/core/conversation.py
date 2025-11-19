"""
Conversation management for IntraMind.

Handles session management, conversation history, and context preservation.
"""

import uuid
from typing import Any, Dict, List, Optional
from dataclasses import dataclass, field
from datetime import datetime
import logging

logger = logging.getLogger(__name__)


@dataclass
class Message:
    """
    Represents a single message in a conversation.

    Attributes:
        role: The role of the message sender (user, assistant, system)
        content: The message content
        timestamp: When the message was created
        metadata: Additional message metadata
    """
    role: str
    content: str
    timestamp: datetime = field(default_factory=datetime.now)
    metadata: Optional[Dict[str, Any]] = None


@dataclass
class ConversationSession:
    """
    Represents a conversation session.

    Attributes:
        session_id: Unique session identifier
        messages: List of messages in the conversation
        context: Session context and metadata
        created_at: Session creation timestamp
        updated_at: Last update timestamp
    """
    session_id: str
    messages: List[Message] = field(default_factory=list)
    context: Dict[str, Any] = field(default_factory=dict)
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)

    def add_message(self, role: str, content: str,
                   metadata: Optional[Dict[str, Any]] = None) -> None:
        """
        Add a message to the conversation.

        Args:
            role: Message role (user, assistant, system)
            content: Message content
            metadata: Optional metadata
        """
        message = Message(role=role, content=content, metadata=metadata)
        self.messages.append(message)
        self.updated_at = datetime.now()
        logger.debug(f"Added message to session {self.session_id}: {role}")

    def get_history(self, limit: Optional[int] = None) -> List[Dict[str, str]]:
        """
        Get conversation history.

        Args:
            limit: Optional limit on number of messages to return

        Returns:
            List of messages as dictionaries
        """
        messages = self.messages[-limit:] if limit else self.messages
        return [
            {
                "role": msg.role,
                "content": msg.content,
                "timestamp": msg.timestamp.isoformat()
            }
            for msg in messages
        ]

    def clear(self) -> None:
        """Clear all messages from the session."""
        self.messages.clear()
        self.updated_at = datetime.now()
        logger.info(f"Cleared session {self.session_id}")


class ConversationManager:
    """
    Manages conversation sessions and their lifecycle.

    This class handles session creation, retrieval, and cleanup,
    ensuring conversation context is properly maintained.
    """

    def __init__(self, config: Any):
        """
        Initialize the ConversationManager.

        Args:
            config: Configuration object
        """
        self.config = config
        self.sessions: Dict[str, ConversationSession] = {}
        logger.info("ConversationManager initialized")

    def create_session(self, session_id: Optional[str] = None,
                      context: Optional[Dict[str, Any]] = None) -> ConversationSession:
        """
        Create a new conversation session.

        Args:
            session_id: Optional custom session ID. If None, generates UUID.
            context: Optional initial context

        Returns:
            Created ConversationSession
        """
        if session_id is None:
            session_id = str(uuid.uuid4())

        session = ConversationSession(
            session_id=session_id,
            context=context or {}
        )
        self.sessions[session_id] = session
        logger.info(f"Created new session: {session_id}")
        return session

    def get_session(self, session_id: str) -> Optional[ConversationSession]:
        """
        Get an existing session.

        Args:
            session_id: Session identifier

        Returns:
            ConversationSession if found, None otherwise
        """
        return self.sessions.get(session_id)

    def get_or_create_session(self, session_id: Optional[str] = None,
                             context: Optional[Dict[str, Any]] = None) -> ConversationSession:
        """
        Get existing session or create new one.

        Args:
            session_id: Optional session identifier
            context: Optional context for new sessions

        Returns:
            ConversationSession
        """
        if session_id and session_id in self.sessions:
            return self.sessions[session_id]
        return self.create_session(session_id, context)

    def clear_session(self, session_id: str) -> bool:
        """
        Clear a session's conversation history.

        Args:
            session_id: Session identifier

        Returns:
            True if session was cleared, False if not found
        """
        session = self.get_session(session_id)
        if session:
            session.clear()
            return True
        return False

    def delete_session(self, session_id: str) -> bool:
        """
        Delete a session entirely.

        Args:
            session_id: Session identifier

        Returns:
            True if session was deleted, False if not found
        """
        if session_id in self.sessions:
            del self.sessions[session_id]
            logger.info(f"Deleted session: {session_id}")
            return True
        return False

    def cleanup_old_sessions(self, max_age_hours: int = 24) -> int:
        """
        Remove sessions older than specified age.

        Args:
            max_age_hours: Maximum age in hours

        Returns:
            Number of sessions removed
        """
        now = datetime.now()
        sessions_to_remove = []

        for session_id, session in self.sessions.items():
            age_hours = (now - session.updated_at).total_seconds() / 3600
            if age_hours > max_age_hours:
                sessions_to_remove.append(session_id)

        for session_id in sessions_to_remove:
            del self.sessions[session_id]

        if sessions_to_remove:
            logger.info(f"Cleaned up {len(sessions_to_remove)} old sessions")

        return len(sessions_to_remove)
