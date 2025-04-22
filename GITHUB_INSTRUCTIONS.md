# Connecting to GitHub

## Add your GitHub repository as the remote origin

Run this command in your terminal, replacing `YOUR_USERNAME` with your GitHub username:

```
git remote add origin https://github.com/YOUR_USERNAME/portfolio.git
```

## Push your code to GitHub

```
git push -u origin master
```

You'll be prompted to enter your GitHub username and password. If you have two-factor authentication enabled, you'll need to use a personal access token instead of your password.

## Creating a Personal Access Token (if needed)

1. Go to GitHub Settings → Developer Settings → Personal Access Tokens
2. Click "Generate new token"
3. Give it a name like "Portfolio Access"
4. Select the "repo" scope
5. Click "Generate token"
6. Copy the token and use it as your password when pushing

## Hosting with GitHub Pages (Optional)

You can host your portfolio directly from your GitHub repository using GitHub Pages:

1. Go to your repository on GitHub
2. Click on "Settings"
3. Scroll down to the "GitHub Pages" section
4. Under "Source", select "master" branch (or "main" if that's what you're using)
5. Click "Save"

Your site will be published at `https://YOUR_USERNAME.github.io/portfolio/` (replace YOUR_USERNAME with your GitHub username).

## Making Updates

Whenever you want to update your portfolio:

1. Make your changes locally
2. Commit them: `git add . && git commit -m "Description of changes"`
3. Push to GitHub: `git push origin master` (or `main`)
4. If using GitHub Pages, your site will automatically update within a few minutes