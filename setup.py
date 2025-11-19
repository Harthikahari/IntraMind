"""
Setup configuration for IntraMind.
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read the README file
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")

# Read requirements
requirements = (this_directory / "requirements.txt").read_text(encoding="utf-8").splitlines()

setup(
    name="intramind",
    version="1.0.0",
    author="IntraMind Team",
    author_email="dev@intramind.ai",
    description="Enterprise-Grade AI Conversational Chatbot Platform",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/IntraMind",
    project_urls={
        "Bug Tracker": "https://github.com/yourusername/IntraMind/issues",
        "Documentation": "https://docs.intramind.ai",
        "Source Code": "https://github.com/yourusername/IntraMind",
    },
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
        "Topic :: Communications :: Chat",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
        "Framework :: FastAPI",
    ],
    python_requires=">=3.9",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=7.4.0",
            "pytest-asyncio>=0.21.0",
            "pytest-cov>=4.1.0",
            "black>=23.0.0",
            "flake8>=6.0.0",
            "mypy>=1.0.0",
            "pylint>=3.0.0",
            "isort>=5.12.0",
        ],
        "docs": [
            "mkdocs>=1.5.0",
            "mkdocs-material>=9.0.0",
            "mkdocstrings[python]>=0.24.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "intramind=main:main",
        ],
    },
    include_package_data=True,
    zip_safe=False,
    keywords="chatbot ai nlp conversational-ai llm openai enterprise document-intelligence",
)
