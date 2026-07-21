"""Milestone 1 smoke tests — confirms routing, layout, and static assets work."""
import pytest

from app import create_app


@pytest.fixture
def client():
    app = create_app("testing")
    with app.test_client() as client:
        yield client


@pytest.mark.parametrize(
    "path",
    ["/", "/about", "/services", "/portfolio", "/contact"],
)
def test_pages_return_200(client, path):
    response = client.get(path)
    assert response.status_code == 200


def test_unknown_route_returns_404(client):
    response = client.get("/this-page-does-not-exist")
    assert response.status_code == 404


def test_home_page_contains_brand_and_layout(client):
    response = client.get("/")
    html = response.get_data(as_text=True)
    assert "D-TECH DYNAMICS" in html
    assert '<nav class="navbar">' in html
    assert '<footer class="footer">' in html


def test_about_page_contains_team_and_values(client):
    response = client.get("/about")
    html = response.get_data(as_text=True)
    assert "Our Core Values" in html
    assert "Marcus Reyes" in html


def test_services_page_contains_all_six_services(client):
    response = client.get("/services")
    html = response.get_data(as_text=True)
    for service_name in [
        "Cybersecurity",
        "Software Development",
        "IT Consulting",
        "Network Solutions",
        "Automation",
        "Cloud Services",
    ]:
        assert service_name in html


@pytest.mark.parametrize(
    "asset_path",
    [
        "/static/css/main.css",
        "/static/css/variables.css",
        "/static/js/main.js",
        "/static/images/dtech-logo.png",
    ],
)
def test_static_assets_are_served(client, asset_path):
    response = client.get(asset_path)
    assert response.status_code == 200
