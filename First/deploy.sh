#!/bin/bash

echo "🚀 GitHub Pages Deployment Script for RevealJS Presentation"
echo "========================================================="

# Check if we're in a git repository
if [ ! -d ".git" ]; then
    echo "❌ Error: Not in a git repository"
    echo "Initialize git first with: git init"
    exit 1
fi

# Check if remote origin exists
if ! git remote get-url origin &> /dev/null; then
    echo "❌ Error: No remote origin found"
    echo "Add remote origin first with: git remote add origin https://github.com/username/repository.git"
    exit 1
fi

echo "📁 Current directory: $(pwd)"
echo "📋 Files to be deployed:"
ls -la First/

echo ""
read -p "🤔 Ready to deploy to GitHub Pages? (y/N): " confirm

if [[ $confirm == [yY] || $confirm == [yY][eE][sS] ]]; then
    echo ""
    echo "📤 Adding files to git..."
    git add .
    
    echo "💾 Committing changes..."
    git commit -m "Deploy RevealJS earnings presentation to GitHub Pages"
    
    echo "🌐 Pushing to GitHub..."
    git push origin main
    
    echo ""
    echo "✅ Files pushed to GitHub successfully!"
    echo ""
    echo "📖 Next steps to enable GitHub Pages:"
    echo "1. Go to your repository on GitHub.com"
    echo "2. Click 'Settings' tab"
    echo "3. Scroll to 'Pages' section"
    echo "4. Under 'Source', select 'Deploy from a branch'"
    echo "5. Choose 'main' branch and '/ (root)' folder"
    echo "6. Click 'Save'"
    echo ""
    echo "🌍 Your presentation will be available at:"
    
    # Try to get the repository URL and construct Pages URL
    REPO_URL=$(git remote get-url origin)
    if [[ $REPO_URL == *"github.com"* ]]; then
        # Extract username and repository name
        REPO_PATH=$(echo $REPO_URL | sed 's/.*github\.com[:/]\([^/]*\/[^/]*\)\.git/\1/')
        echo "   https://${REPO_PATH%/*}.github.io/${REPO_PATH#*/}/First/"
    else
        echo "   https://[username].github.io/[repository-name]/First/"
    fi
    
    echo ""
    echo "⏰ Note: GitHub Pages deployment may take a few minutes"
    
else
    echo "❌ Deployment cancelled"
fi
