import pytest
from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_shorten_url():
    response = client.post("/shorten", json={"url": "https://www.example.com"})
    assert response.status_code == 200
    assert "shorten_url" in response.json()


def test_redirect_to_original():
    response = client.post("/shorten", json={"url": "https://www.example.com"})
    short_url = response.json()["shorten_url"].split("/")[-1]
    redirect_response = client.get(f"/{short_url}", follow_redirects=False)
    assert redirect_response.status_code == 307
    assert redirect_response.headers["location"] == "https://www.example.com"


def test_invalid_url():
    response = client.post("/shorten", json={"url": "invalid_url"})
    assert response.status_code == 400
    assert response.json() == {"detail": "URL is not valid"}


@pytest.mark.parametrize("url, expected_status", [
    ("https://github.com/jeetendra29gupta/URL-Shortener-Service", 200),  # Valid URL
    ("github.com", 400),  # Invalid URL
])
def test_shorten_url_endpoint(url, expected_status):
    response = client.post("/shorten", json={"url": url})
    assert response.status_code == expected_status
