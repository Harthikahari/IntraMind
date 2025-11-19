# Contributing to IntraMind

First off, thank you for considering contributing to IntraMind! It's people like you that make IntraMind such a great tool.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Process](#development-process)
- [How to Contribute](#how-to-contribute)
- [Style Guidelines](#style-guidelines)
- [Testing Guidelines](#testing-guidelines)
- [Commit Guidelines](#commit-guidelines)
- [Pull Request Process](#pull-request-process)

## Code of Conduct

This project and everyone participating in it is governed by our Code of Conduct. By participating, you are expected to uphold this code. Please report unacceptable behavior to [conduct@intramind.ai](mailto:conduct@intramind.ai).

### Our Standards

- Using welcoming and inclusive language
- Being respectful of differing viewpoints and experiences
- Gracefully accepting constructive criticism
- Focusing on what is best for the community
- Showing empathy towards other community members

## Getting Started

### Prerequisites

- Python 3.9 or higher
- Git
- PostgreSQL 13+
- Redis 6+
- Basic understanding of async Python and FastAPI

### Setting Up Your Development Environment

1. **Fork the repository** on GitHub

2. **Clone your fork**
   ```bash
   git clone https://github.com/YOUR_USERNAME/IntraMind.git
   cd IntraMind
   ```

3. **Add upstream remote**
   ```bash
   git remote add upstream https://github.com/original/IntraMind.git
   ```

4. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

5. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   pip install -r requirements-dev.txt
   ```

6. **Set up pre-commit hooks**
   ```bash
   pre-commit install
   ```

7. **Configure environment**
   ```bash
   cp .env.example .env
   # Edit .env with your local configuration
   ```

8. **Initialize the database**
   ```bash
   python scripts/init_db.py
   ```

9. **Run tests to verify setup**
   ```bash
   pytest
   ```

## Development Process

### Branching Strategy

We use a simplified Git Flow:

- `main` - Production-ready code
- `develop` - Integration branch for features
- `feature/*` - New features
- `bugfix/*` - Bug fixes
- `hotfix/*` - Urgent production fixes
- `docs/*` - Documentation updates

### Workflow

1. **Sync with upstream**
   ```bash
   git checkout develop
   git pull upstream develop
   ```

2. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make your changes**
   - Write code
   - Add tests
   - Update documentation

4. **Run tests and checks**
   ```bash
   # Format code
   black src/ tests/
   isort src/ tests/

   # Lint
   flake8 src/ tests/
   pylint src/

   # Type check
   mypy src/

   # Run tests
   pytest
   ```

5. **Commit your changes**
   ```bash
   git add .
   git commit -m "feat: add amazing feature"
   ```

6. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```

7. **Open a Pull Request** on GitHub

## How to Contribute

### Reporting Bugs

Before creating bug reports, please check the issue list as you might find out that you don't need to create one. When you are creating a bug report, please include as many details as possible:

- **Use a clear and descriptive title**
- **Describe the exact steps to reproduce the problem**
- **Provide specific examples**
- **Describe the behavior you observed and what you expected**
- **Include screenshots if relevant**
- **Include your environment details** (OS, Python version, etc.)

**Bug Report Template:**

```markdown
**Description:**
A clear description of the bug.

**Steps to Reproduce:**
1. Go to '...'
2. Click on '....'
3. Scroll down to '....'
4. See error

**Expected Behavior:**
What you expected to happen.

**Actual Behavior:**
What actually happened.

**Environment:**
- OS: [e.g., Ubuntu 22.04]
- Python Version: [e.g., 3.11.0]
- IntraMind Version: [e.g., 1.0.0]

**Additional Context:**
Any other information about the problem.
```

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion, please include:

- **Use a clear and descriptive title**
- **Provide a detailed description of the suggested enhancement**
- **Explain why this enhancement would be useful**
- **List some examples of how it would be used**

### Your First Code Contribution

Unsure where to begin? You can start by looking through these issues:

- `good-first-issue` - Issues good for newcomers
- `help-wanted` - Issues that need assistance

### Pull Requests

- Fill in the required template
- Follow the style guidelines
- Include tests for new features
- Update documentation as needed
- Ensure all tests pass
- Link related issues

## Style Guidelines

### Python Style Guide

We follow PEP 8 with some modifications:

- **Line length**: 100 characters (not 79)
- **Indentation**: 4 spaces
- **Quotes**: Double quotes for strings
- **Imports**: Organized with isort

#### Code Formatting

We use **Black** for code formatting:

```bash
black src/ tests/
```

#### Import Organization

We use **isort** for import sorting:

```bash
isort src/ tests/
```

#### Type Hints

All functions should have type hints:

```python
def process_message(message: str, user_id: int) -> dict[str, Any]:
    """Process a user message and return response."""
    pass
```

#### Docstrings

Use Google-style docstrings:

```python
def complex_function(param1: str, param2: int) -> bool:
    """
    Brief description of the function.

    Longer description if needed, explaining what the function does,
    its purpose, and any important details.

    Args:
        param1: Description of param1
        param2: Description of param2

    Returns:
        Description of return value

    Raises:
        ValueError: When something goes wrong

    Examples:
        >>> complex_function("test", 42)
        True
    """
    pass
```

### Git Commit Messages

We follow the [Conventional Commits](https://www.conventionalcommits.org/) specification:

#### Format

```
<type>(<scope>): <subject>

<body>

<footer>
```

#### Types

- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, etc.)
- `refactor`: Code refactoring
- `test`: Adding or updating tests
- `chore`: Maintenance tasks
- `perf`: Performance improvements
- `ci`: CI/CD changes

#### Examples

```
feat(chat): add sentiment analysis to responses

Implemented sentiment analysis using transformers library.
This allows the bot to detect user emotions and adapt responses.

Closes #123
```

```
fix(api): resolve rate limiting issue

Fixed bug where rate limiting was not properly applied to
WebSocket connections.

Fixes #456
```

## Testing Guidelines

### Writing Tests

- Write tests for all new features
- Maintain or improve code coverage
- Use descriptive test names
- Follow the Arrange-Act-Assert pattern

#### Example Test

```python
import pytest
from intramind.core.chat import ChatBot


class TestChatBot:
    """Test suite for ChatBot class."""

    def test_basic_response(self):
        """Test that bot returns a response to a simple message."""
        # Arrange
        bot = ChatBot()
        message = "Hello"

        # Act
        response = bot.chat(message)

        # Assert
        assert response is not None
        assert isinstance(response.message, str)
        assert len(response.message) > 0

    @pytest.mark.asyncio
    async def test_async_response(self):
        """Test async chat functionality."""
        # Arrange
        bot = ChatBot()
        message = "What's the weather?"

        # Act
        response = await bot.chat_async(message)

        # Assert
        assert response.status == "success"
```

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src/intramind --cov-report=html

# Run specific test file
pytest tests/unit/test_chat.py

# Run specific test
pytest tests/unit/test_chat.py::TestChatBot::test_basic_response

# Run with verbose output
pytest -v

# Run and stop on first failure
pytest -x
```

## Pull Request Process

1. **Ensure your PR**:
   - Passes all tests
   - Follows style guidelines
   - Includes tests for new features
   - Updates relevant documentation
   - Has a clear description

2. **PR Title**: Follow commit message format
   ```
   feat(scope): brief description
   ```

3. **PR Description**: Use the template provided

4. **Review Process**:
   - At least one maintainer must approve
   - All CI checks must pass
   - All discussions must be resolved

5. **After Approval**:
   - Squash and merge (usually)
   - Delete your branch after merge

### PR Template

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Testing
- [ ] All tests pass
- [ ] New tests added
- [ ] Manual testing completed

## Checklist
- [ ] Code follows style guidelines
- [ ] Self-review completed
- [ ] Comments added for complex code
- [ ] Documentation updated
- [ ] No new warnings generated
- [ ] Tests added/updated
- [ ] All tests passing

## Related Issues
Closes #(issue number)

## Screenshots (if applicable)
```

## Questions?

Don't hesitate to ask questions! You can:

- Open an issue with the `question` label
- Join our [Discord community](https://discord.gg/intramind)
- Email us at [dev@intramind.ai](mailto:dev@intramind.ai)

## Recognition

Contributors are recognized in:

- The project README
- Release notes
- Our [Contributors page](https://intramind.ai/contributors)

Thank you for contributing to IntraMind! 🎉
