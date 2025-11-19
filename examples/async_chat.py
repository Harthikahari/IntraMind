"""
Async chat example for IntraMind.

This example demonstrates asynchronous chat for high-performance applications.
"""

import asyncio
from intramind import ChatBot


async def process_message(bot: ChatBot, message: str, session_id: str):
    """Process a single message asynchronously."""
    response = await bot.chat_async(message, session_id=session_id)
    print(f"User: {message}")
    print(f"Bot: {response.message}\n")
    return response


async def main():
    """Run async chat examples."""
    print("="*60)
    print("  IntraMind - Async Chat Example")
    print("="*60 + "\n")

    # Initialize chatbot
    bot = ChatBot()
    session_id = "async-demo-001"

    # Example 1: Sequential async messages
    print("Example 1: Sequential Async Messages")
    print("-" * 40)

    messages = [
        "Hello!",
        "How are you?",
        "Tell me about your capabilities"
    ]

    for message in messages:
        await process_message(bot, message, session_id)

    # Example 2: Concurrent processing of multiple messages
    print("\nExample 2: Concurrent Message Processing")
    print("-" * 40)

    sessions = ["session-1", "session-2", "session-3"]
    tasks = [
        process_message(bot, f"Hello from session {i+1}", session)
        for i, session in enumerate(sessions)
    ]

    # Process all messages concurrently
    await asyncio.gather(*tasks)

    print("="*60)
    print("  Async example completed successfully!")
    print("="*60)


if __name__ == "__main__":
    asyncio.run(main())
