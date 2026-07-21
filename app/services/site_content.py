"""
Site content — structured data for marketing pages.

This is intentionally plain Python data (no database) since the site has
no CMS yet. Centralizing it here means Milestone 3 (Services) and
Milestone 4 (Portfolio) can reuse these same records instead of
duplicating copy across templates.
"""


def get_services():
    """Six core service lines, shown on Home (overview) and Services (full)."""
    return [
        {
            "icon": "shield",
            "title": "Cybersecurity",
            "summary": "Threat detection, penetration testing, and hardened "
                       "infrastructure built to protect what matters most.",
            "features": [
                "Penetration testing & vulnerability assessments",
                "Real-time threat monitoring and response",
                "Security audits and compliance readiness",
            ],
        },
        {
            "icon": "code",
            "title": "Software Development",
            "summary": "Custom applications and platforms engineered for "
                       "performance, maintainability, and scale.",
            "features": [
                "Custom web and internal business applications",
                "API design and third-party integrations",
                "Legacy system modernization",
            ],
        },
        {
            "icon": "consult",
            "title": "IT Consulting",
            "summary": "Strategic technology guidance to align infrastructure "
                       "decisions with long-term business goals.",
            "features": [
                "Technology roadmaps and architecture reviews",
                "Vendor and tooling evaluation",
                "IT budget and resourcing strategy",
            ],
        },
        {
            "icon": "network",
            "title": "Network Solutions",
            "summary": "Resilient network architecture, monitoring, and "
                       "support for organizations of any size.",
            "features": [
                "Network design and infrastructure buildout",
                "Ongoing monitoring and maintenance",
                "Disaster recovery and failover planning",
            ],
        },
        {
            "icon": "automation",
            "title": "Automation",
            "summary": "Workflow and infrastructure automation that reduces "
                       "manual overhead and human error.",
            "features": [
                "CI/CD pipeline design and implementation",
                "Business process and workflow automation",
                "Infrastructure-as-code deployment",
            ],
        },
        {
            "icon": "cloud",
            "title": "Cloud Services",
            "summary": "Cloud migration, architecture, and management across "
                       "modern, cost-efficient environments.",
            "features": [
                "Cloud migration with minimal downtime",
                "Multi-cloud and hybrid architecture",
                "Cost optimization and ongoing management",
            ],
        },
    ]


def get_differentiators():
    """"Why choose D-Tech" pillars shown on the home page."""
    return [
        {
            "title": "Security-First Engineering",
            "summary": "Every solution is built with protection in mind from "
                       "day one, not bolted on afterward.",
        },
        {
            "title": "Proven Technical Depth",
            "summary": "A senior team fluent across security, software, and "
                       "infrastructure disciplines.",
        },
        {
            "title": "Built to Scale",
            "summary": "Architecture decisions made for where your business "
                       "is going, not just where it is today.",
        },
        {
            "title": "Dedicated Partnership",
            "summary": "Direct access to the people building your systems — "
                       "no account-manager layers.",
        },
    ]


def get_featured_projects(limit=None):
    """Representative project cards for Home (featured) and Portfolio (full)."""
    projects = [
        {
            "title": "Enterprise Threat Detection Platform",
            "category": "Cybersecurity",
            "summary": "A real-time monitoring platform that flags anomalous "
                       "network activity before it becomes an incident.",
        },
        {
            "title": "Cloud Migration for Regional Retailer",
            "category": "Cloud Services",
            "summary": "Full infrastructure migration to a modern cloud "
                       "environment with zero downtime during cutover.",
        },
        {
            "title": "Automated DevOps Pipeline",
            "category": "Automation",
            "summary": "CI/CD pipeline automation that cut deployment time "
                       "from hours to minutes across every environment.",
        },
    ]
    return projects[:limit] if limit else projects


def get_values():
    """Core company values shown on the About page."""
    return [
        {
            "icon": "shield",
            "title": "Integrity by Default",
            "summary": "We tell clients what they need to hear, not what's "
                       "easiest — especially when it comes to security.",
        },
        {
            "icon": "code",
            "title": "Craft Over Shortcuts",
            "summary": "Clean, documented, maintainable work — every time, "
                       "not just when someone's watching.",
        },
        {
            "icon": "network",
            "title": "Resilience First",
            "summary": "Systems are designed to withstand failure, not just "
                       "perform well when everything goes right.",
        },
        {
            "icon": "consult",
            "title": "Genuine Partnership",
            "summary": "We work alongside your team, with full transparency, "
                       "not as a vendor issuing invoices.",
        },
    ]


def get_team():
    """Leadership team shown on the About page."""
    return [
        {
            "name": "Marcus Reyes",
            "role": "Founder & Chief Executive Officer",
            "bio": "Sets the technical vision and leads D-Tech's largest "
                   "client engagements.",
            "initials": "MR",
        },
        {
            "name": "Elena Voss",
            "role": "Head of Cybersecurity",
            "bio": "Leads threat detection and penetration testing across "
                   "every client environment.",
            "initials": "EV",
        },
        {
            "name": "Jamal Ortiz",
            "role": "Lead Software Architect",
            "bio": "Oversees platform architecture and engineering standards "
                   "for custom builds.",
            "initials": "JO",
        },
        {
            "name": "Priya Nair",
            "role": "Director of Cloud & Infrastructure",
            "bio": "Runs cloud migrations and infrastructure automation "
                   "engagements end to end.",
            "initials": "PN",
        },
    ]
