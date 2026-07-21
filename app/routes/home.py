"""
=========================================================
 D-Tech Dynamics Platform
 Home Blueprint

 Author : D-Tech Dynamics
 Version: 1.0.0
=========================================================
"""

from flask import Blueprint, render_template


# ==========================================================
# Blueprint
# ==========================================================

home_bp = Blueprint(
    "home",
    __name__
)


# ==========================================================
# Home
# ==========================================================

@home_bp.route("/")
def home():

    return render_template(
        "home/index.html"
    )