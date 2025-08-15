# Quarterly Earnings Presentation - RevealJS

A professional interactive presentation for Q3 2025 quarterly earnings report built with RevealJS.

## Features

- 📊 **Interactive Financial Metrics** - Animated charts and key performance indicators
- 📝 **Markdown Content** - Executive summary written in Markdown
- 🎬 **Fragment Animations** - Smooth reveal animations for content
- 💻 **Syntax Highlighting** - Python and JavaScript code samples with proper highlighting
- 🧮 **Mathematical Equations** - Financial formulas rendered with KaTeX
- 🎤 **Speaker Notes** - Comprehensive presentation guidance notes
- 📱 **Responsive Design** - Works on desktop, tablet, and mobile devices

## Local Development

1. Clone this repository
2. Navigate to the `First` folder
3. Open `index.html` in a web browser
4. Use arrow keys or click to navigate through slides
5. Press 'S' to open speaker notes view

## GitHub Pages Deployment Instructions

### Method 1: Using GitHub Web Interface

1. **Push your code to GitHub:**
   ```bash
   git add .
   git commit -m "Add RevealJS earnings presentation"
   git push origin main
   ```

2. **Enable GitHub Pages:**
   - Go to your repository on GitHub.com
   - Click on "Settings" tab
   - Scroll down to "Pages" section in the left sidebar
   - Under "Source", select "Deploy from a branch"
   - Choose "main" branch
   - Select "/ (root)" as the folder
   - Click "Save"

3. **Configure for subfolder (if needed):**
   - If you want to serve from the `First` folder specifically:
   - Change the folder selection to "/First" if available
   - Or move the `index.html` to the root directory

4. **Access your presentation:**
   - GitHub will provide a URL like: `https://[username].github.io/[repository-name]/`
   - If serving from First folder: `https://[username].github.io/[repository-name]/First/`

### Method 2: Using GitHub CLI

```bash
# Make sure you're in the repository root
cd /workspaces/Week7

# Add all files
git add .

# Commit changes
git commit -m "Add interactive RevealJS earnings presentation"

# Push to main branch
git push origin main

# Enable GitHub Pages using GitHub CLI (if installed)
gh repo edit --enable-pages --pages-branch main --pages-path /First
```

### Method 3: Using GitHub Actions (Advanced)

Create `.github/workflows/pages.yml`:

```yaml
name: Deploy RevealJS to Pages

on:
  push:
    branches: [ main ]
  workflow_dispatch:

permissions:
  contents: read
  pages: write
  id-token: write

concurrency:
  group: "pages"
  cancel-in-progress: false

jobs:
  deploy:
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4
      
      - name: Setup Pages
        uses: actions/configure-pages@v4
      
      - name: Upload artifact
        uses: actions/upload-pages-artifact@v3
        with:
          path: './First'
      
      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v4
```

## Presentation Controls

- **Navigation:** Arrow keys, space bar, or click
- **Overview:** Press ESC to see all slides
- **Speaker Notes:** Press 'S' to open speaker view
- **Fullscreen:** Press 'F'
- **Help:** Press '?'

## Customization

### Themes
Change the theme by modifying the CSS link in `index.html`:
```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@4.6.1/dist/theme/[THEME_NAME].css">
```

Available themes: black, white, league, sky, beige, simple, serif, blood, night, moon, solarized

### Adding Slides
Add new sections between the existing `<section>` tags:
```html
<section>
    <h2>Your Slide Title</h2>
    <p>Your content here</p>
    <aside class="notes">
        Speaker notes for this slide
    </aside>
</section>
```

### Mathematical Equations
Use LaTeX syntax for mathematical formulas:
```html
<p>$$\text{Your Formula} = \frac{a}{b}$$</p>
```

## File Structure

```
First/
├── index.html          # Main presentation file
└── README.md          # This documentation
```

## Dependencies

All dependencies are loaded via CDN:
- RevealJS 4.6.1
- KaTeX for mathematical equations
- Highlight.js for syntax highlighting
- Font Awesome for icons

## Contact

**Technical Consultant**  
Email: 23f1001177@ds.study.iitm.ac.in

## License

This presentation is created for educational and professional demonstration purposes.
