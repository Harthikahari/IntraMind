#!/bin/bash

echo "========================================="
echo "  IntraMind GitHub Push Script"
echo "========================================="
echo ""
echo "This script will push IntraMind to GitHub"
echo ""

# Check if in correct directory
if [ ! -f "README.md" ] || [ ! -d "src" ]; then
    echo "❌ Error: Please run this script from the IntraMind directory"
    exit 1
fi

echo "📋 Repository Status:"
echo ""
git status --short
echo ""

echo "📊 What will be pushed:"
git log --oneline -n 3
echo ""

read -p "Do you want to push to GitHub? (y/n): " -n 1 -r
echo ""

if [[ $REPLY =~ ^[Yy]$ ]]; then
    echo ""
    echo "🚀 Pushing to GitHub..."
    echo ""

    # Try to push
    git push -u origin main

    if [ $? -eq 0 ]; then
        echo ""
        echo "✅ Successfully pushed to GitHub!"
        echo ""
        echo "🌐 Your repository: https://github.com/Harthikahari/IntraMind"
        echo "📄 Landing page will be available at: https://harthikahari.github.io/IntraMind/"
        echo ""
        echo "📝 Next steps:"
        echo "1. Enable GitHub Pages in repository settings"
        echo "2. Select 'main' branch and '/ (root)' folder"
        echo "3. Your landing page will be live!"
        echo ""
    else
        echo ""
        echo "❌ Push failed. Please check:"
        echo "1. Repository exists: https://github.com/Harthikahari/IntraMind"
        echo "2. You have push permissions"
        echo "3. Remote URL is correct: git remote -v"
        echo ""
        echo "💡 Create the repository first:"
        echo "   Go to: https://github.com/new"
        echo "   Name: IntraMind"
        echo "   Don't initialize with README"
        echo ""
    fi
else
    echo ""
    echo "❌ Push cancelled"
    echo ""
fi
