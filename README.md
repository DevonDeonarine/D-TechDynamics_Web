# D-Tech Dynamics — Website

Production-track Flask website for D-Tech Dynamics (Technology Solutions,
Cybersecurity, Software Development, IT Consulting, Digital Services).

## Status: Milestone 3 — About & Services ✅

About and Services are now fully built out. Portfolio and Contact still show
their Milestone 1 scaffold notice pending Milestone 4.

New files added this milestone, each justified:

- `app/static/css/shared.css` — the service cards, differentiator/value
  cards, section headers, and CTA band are used on Home, About, *and*
  Services. Pulling them out of `home.css` into a shared file avoids
  duplicating the same CSS three times (violates the "no duplicated code"
  standard otherwise).
- `app/static/css/pages/about.css` — About-only styles (story layout, team
  cards) that don't belong in the shared file since no other page uses them.
- `app/templates/components/page_header.html` — a small reusable page-title
  banner used by About, Services, and (in Milestone 4) Portfolio and Contact,
  instead of repeating the same markup four times.
- `site_content.py` gained `get_values()` and `get_team()` for the About
  page, and each service record gained a `features` list for the full
  Services page — both additive, no breaking changes to Home.

## Milestone Plan

1. **Foundation** ✅ — Flask app factory, config, blueprint structure, base
   layout, navbar, footer, design tokens, error pages.
2. **Home page** ✅ — hero, company intro, services overview, why D-Tech,
   featured projects, CTA.
3. **About & Services** ✅ — company story, mission, values, team; full
   service detail cards with feature lists.
3. **About & Services** — company story, team, service cards (Cybersecurity,
   Software Development, IT Consulting, Network Solutions, Automation, Cloud).
4. **Portfolio & Contact** — project case-study cards (filter-ready),
   validated contact form (Flask-WTF).
5. **Polish** — responsiveness, accessibility, performance pass.

## Tech Stack

- Python + Flask (Application Factory pattern)
- Jinja2 templates
- Vanilla HTML5 / CSS3 / JavaScript — no React/Vue/Angular/Bootstrap/Tailwind
- Flask-WTF (wired in for Milestone 4's contact form)

## Project Structure

```text
D-TechDynamics_Web/
├── app.py                  # Entry point
├── config.py                # Environment configs
├── requirements.txt
├── app/
│   ├── __init__.py           # Application factory
│   ├── routes/main.py        # Main blueprint (/, /about, /services, /portfolio, /contact)
│   ├── models/                # (empty — reserved for future data models)
│   ├── forms/                  # (empty — Flask-WTF forms land here in Milestone 4)
│   ├── services/
│   │   └── site_content.py     # Services / differentiators / featured project data
│   ├── utils/                   # (empty — shared helpers)
│   ├── static/
│   │   ├── css/
│   │   │   ├── variables.css   # Design tokens (colors, spacing, type)
│   │   │   ├── base.css        # Reset + global layout
│   │   │   ├── components.css  # Navbar, footer, buttons, glass panels, page header
│   │   │   ├── shared.css      # Section headers, service/value cards, CTA band
│   │   │   ├── main.css        # Aggregates the above
│   │   │   └── pages/
│   │   │       ├── home.css    # Hero, intro, featured-project styles
│   │   │       └── about.css   # Story layout, team cards
│   │   ├── js/main.js          # Sticky nav + mobile menu toggle
│   │   └── images/dtech-logo.png
│   └── templates/
│       ├── layouts/base.html    # Shared HTML shell
│       ├── components/          # navbar.html, footer.html, icon.html, page_header.html
│       ├── home/index.html       # Full Milestone 2 build-out
│       ├── about/index.html      # Full Milestone 3 build-out
│       ├── services/index.html   # Full Milestone 3 build-out
│       ├── portfolio/ contact/    # one index.html each (scaffold, pending Milestone 4)
│       └── errors/               # 404.html, 500.html
├── assets/     # source/design assets (not served directly)
├── uploads/     # user-submitted files (e.g. contact attachments, future)
├── instance/    # instance-specific config (gitignored in real deployment)
└── tests/       # pytest suite
```

## Design Language

Tokens live in `app/static/css/variables.css`, derived from the brand mark:

- **Cyan** (`--color-cyan`) — circuitry / technical accent
- **Dragon red** (`--color-red`) — brand accent, used sparingly
- **Near-black background** with soft cyan/red radial glow
- **Glass panels** (`.glass-panel`) — translucent, blurred, subtle border
- **Rajdhani** for headings (technical, geometric), **Inter** for body copy

## Running Locally

```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Visit `http://localhost:5000`.

## Running Tests

```bash
pip install pytest
pytest
```

## Project Rule

**Do not create files that were not requested.** Before adding a new file,
explain why it's necessary. This keeps the codebase lean and maintainable
milestone to milestone.
