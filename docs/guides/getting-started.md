# Getting Started with IntraMind

Welcome to IntraMind! This guide will help you set up and start using the platform.

## Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.9 or higher**: [Download Python](https://www.python.org/downloads/)
- **pip**: Python package installer (usually comes with Python)
- **PostgreSQL 13+**: [Download PostgreSQL](https://www.postgresql.org/download/)
- **Redis 6+**: [Download Redis](https://redis.io/download)
- **Git**: [Download Git](https://git-scm.com/downloads)

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/IntraMind.git
cd IntraMind
```

### 2. Create a Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate

# On Windows:
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

```bash
# Copy the example environment file
cp .env.example .env

# Edit the .env file with your settings
nano .env  # or use your preferred editor
```

**Important environment variables to configure:**

```bash
# AI Provider Configuration (choose one)
AI_PROVIDER=openai
OPENAI_API_KEY=your-api-key-here

# Database
DATABASE_URL=postgresql://username:password@localhost:5432/intramind

# Redis
REDIS_URL=redis://localhost:6379/0

# Security
SECRET_KEY=your-secret-key-here
JWT_SECRET=your-jwt-secret-here
API_KEY=your-api-key-here
```

### 5. Initialize the Database

```bash
python scripts/init_db.py
```

### 6. Run the Application

```bash
python src/main.py
```

The application will start on `http://localhost:8000`

## Quick Start Examples

### Example 1: Basic Chat

```python
from intramind import ChatBot, Config

# Create a chatbot instance
bot = ChatBot()

# Send a message
response = bot.chat("Hello, IntraMind!")
print(response.message)
```

### Example 2: Chat with Session

```python
from intramind import ChatBot

bot = ChatBot()

# Start a conversation with a session ID
session_id = "user-123"

response1 = bot.chat("My name is Alice", session_id=session_id)
print(response1.message)

response2 = bot.chat("What's my name?", session_id=session_id)
print(response2.message)
```

### Example 3: Async Chat

```python
import asyncio
from intramind import ChatBot

async def main():
    bot = ChatBot()
    response = await bot.chat_async("Hello!")
    print(response.message)

asyncio.run(main())
```

## Using the API

### Starting the API Server

```bash
uvicorn src.main:app --reload
```

### API Endpoints

#### POST /api/v1/chat

Send a message to the chatbot:

```bash
curl -X POST http://localhost:8000/api/v1/chat \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -d '{
    "message": "Hello, IntraMind!",
    "session_id": "user-123"
  }'
```

#### WebSocket /ws/chat

Connect via WebSocket for real-time chat:

```javascript
const ws = new WebSocket('ws://localhost:8000/ws/chat');

ws.onopen = () => {
  ws.send(JSON.stringify({
    type: 'message',
    content: 'Hello!',
    session_id: 'user-123'
  }));
};

ws.onmessage = (event) => {
  const data = JSON.parse(event.data);
  console.log('Response:', data.message);
};
```

## Configuration

### AI Provider Setup

#### OpenAI

```bash
AI_PROVIDER=openai
OPENAI_API_KEY=sk-...
OPENAI_MODEL=gpt-4
```

#### Azure OpenAI (Optional)

```bash
AI_PROVIDER=azure
AZURE_OPENAI_API_KEY=...
AZURE_OPENAI_ENDPOINT=https://your-instance.openai.azure.com/
AZURE_OPENAI_DEPLOYMENT=your-deployment-name
```

### Database Configuration

#### PostgreSQL (Recommended)

```bash
DATABASE_URL=postgresql://user:password@localhost:5432/intramind
```

#### SQLite (Development Only)

```bash
DATABASE_URL=sqlite:///./intramind.db
```

## Testing Your Setup

Run the test suite to verify everything is working:

```bash
pytest
```

Run with coverage:

```bash
pytest --cov=src/intramind
```

## Next Steps

- [API Documentation](../api/) - Explore the full API reference
- [Architecture Guide](../architecture/) - Understand the system design
- [Configuration Guide](configuration.md) - Advanced configuration options
- [Deployment Guide](deployment.md) - Deploy to production

## Troubleshooting

### Common Issues

#### Port Already in Use

```bash
# Find the process using port 8000
lsof -i :8000

# Kill the process
kill -9 <PID>
```

#### Database Connection Error

- Ensure PostgreSQL is running
- Verify database credentials in `.env`
- Check database exists: `createdb intramind`

#### Redis Connection Error

- Ensure Redis is running: `redis-cli ping`
- Start Redis: `redis-server`

#### Import Errors

```bash
# Ensure you're in the virtual environment
source venv/bin/activate

# Reinstall dependencies
pip install -r requirements.txt
```

## Getting Help

- [Documentation](../)
- [GitHub Issues](https://github.com/yourusername/IntraMind/issues)
- [Discord Community](https://discord.gg/intramind)
- Email: support@intramind.ai

## What's Next?

Now that you have IntraMind running, you can:

1. Customize the chatbot behavior
2. Integrate with your AI provider
3. Build custom integrations
4. Deploy to production

Happy coding! 🚀
