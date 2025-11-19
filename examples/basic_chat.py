"""
Basic chat example for IntraMind.

This example demonstrates the simplest way to use IntraMind
for basic conversational interactions.
"""

from intramind import ChatBot, Config


def main():
    """Run a basic chat example."""
    print("="*60)
    print("  IntraMind - Basic Chat Example")
    print("="*60 + "\n")

    # Initialize the chatbot with default configuration
    bot = ChatBot()

    # Example 1: Simple greeting
    print("Example 1: Simple Greeting")
    print("-" * 40)
    response = bot.chat("Hello!")
    print(f"User: Hello!")
    print(f"Bot: {response.message}")
    print(f"Intent: {response.intent}")
    print(f"Confidence: {response.confidence}\n")

    # Example 2: Ask a question
    print("Example 2: Asking a Question")
    print("-" * 40)
    response = bot.chat("What can you help me with?")
    print(f"User: What can you help me with?")
    print(f"Bot: {response.message}\n")

    # Example 3: Conversation with context
    print("Example 3: Contextual Conversation")
    print("-" * 40)
    session_id = "demo-session-001"

    response1 = bot.chat("My name is Alice", session_id=session_id)
    print(f"User: My name is Alice")
    print(f"Bot: {response1.message}")

    response2 = bot.chat("What's my name?", session_id=session_id)
    print(f"User: What's my name?")
    print(f"Bot: {response2.message}\n")

    # Example 4: Check conversation history
    print("Example 4: Conversation History")
    print("-" * 40)
    history = bot.get_session_history(session_id)
    for msg in history:
        print(f"{msg['role'].title()}: {msg['content']}")

    print("\n" + "="*60)
    print("  Example completed successfully!")
    print("="*60)


if __name__ == "__main__":
    main()
