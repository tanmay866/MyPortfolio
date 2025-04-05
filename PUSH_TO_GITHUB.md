# Pushing Your Portfolio to GitHub

## Step 1: Push your code to GitHub

Run this command in your terminal:

```
git push -u origin master
```

You'll be prompted to enter your GitHub credentials.

## Step 2: Connect Netlify to GitHub

1. Log in to [Netlify](https://app.netlify.com/)
2. Go to your site dashboard
3. Click on "Site settings"
4. Go to "Build & deploy" → "Continuous Deployment"
5. Under "Build settings", click "Link site to Git"
6. Choose GitHub as your Git provider
7. Authorize Netlify to access your GitHub account
8. Select your portfolio repository
9. Configure the build settings:
   - Build command: leave empty
   - Publish directory: `.` or `./`
10. Click "Deploy site"

## Step 3: Configure Auto-Publishing

Once connected, your Netlify site will automatically rebuild and deploy whenever you push changes to GitHub!

1. Make changes to your portfolio locally
2. Commit the changes: `git add . && git commit -m "Updated portfolio"`
3. Push to GitHub: `git push origin master`
4. Netlify will automatically detect the changes and rebuild your site

## Checking Deployment Status

1. Go to your Netlify dashboard
2. Click on your site
3. Go to the "Deploys" tab to see the status of your deployments

## Troubleshooting

If you encounter any issues:

1. Check Netlify's deploy logs for errors
2. Make sure your repository contains all necessary files (index.html, css, js, etc.)
3. Confirm that the publish directory is set correctly
4. Verify that the .gitignore file isn't excluding important files 