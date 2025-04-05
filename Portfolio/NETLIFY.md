# Deploying your Portfolio to Netlify

Follow these steps to deploy your portfolio website to Netlify:

## Option 1: Deploy using the Netlify UI (Easiest)

1. **Create a Netlify account**:
   - Go to [netlify.com](https://www.netlify.com/)
   - Sign up with GitHub, GitLab, Bitbucket, or email

2. **Deploy your site**:
   - Click on the "Sites" tab in your Netlify dashboard
   - Drag and drop your entire project folder onto the designated area
   - Netlify will automatically upload and deploy your site

3. **Configure your site**:
   - Once deployed, click on "Site settings"
   - Choose a custom domain name or use the free Netlify subdomain
   - Your site will be available at: `https://your-site-name.netlify.app`

## Option 2: Deploy using Git (Recommended for ongoing development)

1. **Create a Git repository** for your portfolio (if you haven't already):
   ```
   git init
   git add .
   git commit -m "Initial commit"
   ```

2. **Push to GitHub/GitLab/Bitbucket**:
   - Create a new repository on GitHub/GitLab/Bitbucket
   - Follow the instructions to push your local repository

3. **Connect to Netlify**:
   - Log in to Netlify
   - Click "New site from Git"
   - Select your Git provider and repository
   - Configure build settings:
     - Leave build command empty
     - Set publish directory to: `.`
   - Click "Deploy site"

## Customizing Your Site

After deployment, you can:

1. **Set up a custom domain**:
   - Go to "Domain settings" in your site dashboard
   - Click "Add custom domain"
   - Follow the instructions to connect your domain

2. **Enable HTTPS**:
   - Netlify automatically provisions SSL certificates
   - Your site will be secure with HTTPS

3. **Configure form handling** (for your contact form):
   - Add `data-netlify="true"` to your form element in index.html
   - Add `<input type="hidden" name="form-name" value="contact">` inside the form
   - Form submissions will appear in the "Forms" tab in Netlify

## Updating Your Site

To update your site:

- If using the drag-and-drop method, simply drag and drop your folder again
- If using Git, push your changes to your repository and Netlify will automatically redeploy 