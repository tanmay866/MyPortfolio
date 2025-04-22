# Pushing Your Portfolio to GitHub

## Step 1: Initialize Git Repository (if not already done)

If you haven't already initialized your repository:

```
git init
git add .
git commit -m "Initial commit"
```

## Step 2: Create a GitHub Repository

1. Go to [GitHub](https://github.com/) and sign in
2. Click the '+' icon in the top right and select 'New repository'
3. Name your repository (e.g., "MyPortfolio")
4. Choose public or private visibility
5. Click "Create repository"

## Step 3: Connect Local Repository to GitHub

Follow the instructions on GitHub to connect your local repository:

```
git remote add origin https://github.com/yourusername/your-repo-name.git
git branch -M main
git push -u origin main
```

You'll be prompted to enter your GitHub credentials.

## Step 4: Making Future Updates

1. Make changes to your portfolio locally
2. Stage your changes: `git add .`
3. Commit your changes: `git commit -m "Description of changes"`
4. Push to GitHub: `git push origin main`

## Step 5: Using GitHub Pages (Optional)

To host your portfolio using GitHub Pages:

1. Go to your repository on GitHub
2. Click on "Settings"
3. Scroll down to the "GitHub Pages" section
4. Under "Source", select "main" branch
5. Click "Save"
6. Your site will be published at `https://yourusername.github.io/your-repo-name/`

## Troubleshooting

If you encounter any issues:

1. Make sure your repository contains all necessary files (index.html, css, js, etc.)
2. Verify that the .gitignore file isn't excluding important files
3. Check that file paths are correct (relative paths work best for GitHub Pages)
4. Ensure all assets (images, scripts, etc.) are properly included in your repository