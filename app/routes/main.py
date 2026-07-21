"""
Main blueprint — routing for the core public pages.

NOTE (Milestone 1 — Foundation):
Each view below renders a lightweight scaffold template so the routing,
navigation, and base layout can be verified end-to-end. Real page content
is built out in later milestones:
    Milestone 2 -> Home
    Milestone 3 -> About, Services
    Milestone 4 -> Portfolio, Contact
"""
from flask import Blueprint, render_template

from app.services.site_content import (
    get_differentiators,
    get_featured_projects,
    get_services,
    get_team,
    get_values,
)

main_bp = Blueprint("main", __name__)


@main_bp.route("/")
def index():
    return render_template(
        "home/index.html",
        page_title="Home",
        services=get_services(),
        differentiators=get_differentiators(),
        featured_projects=get_featured_projects(limit=3),
    )


@main_bp.route("/about")
def about():
    return render_template(
        "about/index.html",
        page_title="About",
        values=get_values(),
        team=get_team(),
    )


@main_bp.route("/services")
def services():
    return render_template(
        "services/index.html",
        page_title="Services",
        services=get_services(),
    )


@main_bp.route("/portfolio")
def portfolio():
    return render_template("portfolio/index.html", page_title="Portfolio")


@main_bp.route("/contact")
def contact():
    return render_template("contact/index.html", page_title="Contact")
