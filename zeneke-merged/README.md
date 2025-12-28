# Zeneke - Merged Site

This is a merged and migrated version of the Zeneke website, combining:
- Original Jekyll-based blog and articles
- Zensical-based cloud security documentation

## Migration Summary

### What Was Migrated

#### From Jekyll Site
- **9 blog posts** (2013-2016) → `docs/blog/`
- **HTML articles** converted to Markdown → `docs/articles/`
  - Raspberry Pi configuration guide
  - Piratas vs Ninjas game project
- **Static projects** → `docs/projects/`
  - map-guess
  - promoantares
  - graph
  - map
  - riogrande
- **Images and assets** → Copied to respective article folders

#### From Zensical Site
- **Azure documentation** → `docs/azure/`
- **AWS documentation** → `docs/aws/`
- All Zensical configuration and theme

### Structure

```
zeneke-merged/
├── docs/
│   ├── index.md              # New homepage
│   ├── blog/                 # Migrated Jekyll posts
│   │   ├── index.md
│   │   └── *.md             # 8 blog posts
│   ├── articles/            # Converted HTML articles
│   │   ├── raspberry/       # RPi guides
│   │   └── cerdigres/       # Game project
│   ├── projects/            # Static projects
│   │   ├── map-guess/
│   │   ├── promoantares/
│   │   ├── graph/
│   │   ├── map/
│   │   └── riogrande/
│   ├── azure/               # From Zensical
│   ├── aws/                 # From Zensical
│   └── markdown.md          # Markdown guide
├── public/                  # Build output
├── zensical.toml           # Main configuration
└── netlify.toml            # Deployment config
```

## Configuration Changes

### Site Metadata
- **Site Name**: "Zeneke - Cloud Security & Development"
- **Description**: "Technical blog and documentation covering cloud security, game development, and software projects by Zeneke."
- **Copyright**: "Copyright © 2013-2025 Zeneke"

### Navigation
Organized into 5 main sections:
1. **Blog** - Chronological posts (2013-2016)
2. **Cloud Security** - Azure and AWS documentation
3. **Articles** - In-depth guides (Raspberry Pi, game dev)
4. **Projects** - Interactive demos and applications
5. **Markdown Guide** - Zensical markdown reference

## Building the Site

### Requirements
- Zensical CLI tool

### Commands
```bash
# Start development server
zensical serve

# Build for production
zensical build

# Output will be in public/ directory
```

## Content Notes

### Converted Content
- Jekyll posts were stripped of front matter and converted to clean markdown
- HTML articles were simplified to markdown while preserving core content
- Some complex HTML formatting was simplified for better markdown compatibility
- Internal links were updated to work with Zensical structure

### Preserved Assets
- Project folders (map-guess, graph, etc.) copied as-is
- Images from articles copied to appropriate locations
- Favicon preserved

### Not Migrated
- Jekyll layouts and templates (replaced by Zensical theme)
- Custom CSS/SASS (Zensical theme provides styling)
- Some complex HTML-only articles (gamedev multi-part series simplified)

## Deployment

The site is configured for Netlify deployment via `netlify.toml`.

## Original Sites

- **Jekyll site**: Root directory (www.zeneke.com)
- **Zensical site**: `zensical/` folder
- **Merged site**: `zeneke-merged/` folder (this directory)

## Next Steps

1. Review content for accuracy
2. Test all internal links
3. Add any missing content from HTML articles
4. Customize Zensical theme if desired
5. Deploy to hosting platform
6. Set up custom domain

---

*Migration completed: December 2025*
