from fastapi.testclient import TestClient


def test_search_page_returns_html(client: TestClient):
    """Test that search page returns HTML content."""
    response = client.get("/search/")

    assert response.status_code == 200
    assert response.headers["content-type"] == "text/html; charset=utf-8"
    assert "<!DOCTYPE html>" in response.text or "<html" in response.text


def test_search_page_with_query_returns_html(client: TestClient):
    """Test that search page with query parameter returns HTML content."""
    response = client.get("/search/?q=test")

    assert response.status_code == 200
    assert response.headers["content-type"] == "text/html; charset=utf-8"
    assert "<!DOCTYPE html>" in response.text or "<html" in response.text


def test_search_page_contains_search_query(client: TestClient):
    """Test that search page contains the search query in the response."""
    query = "python"
    response = client.get(f"/search/?q={query}")

    assert response.status_code == 200
    assert query in response.text


def test_search_page_contains_results_for_query(client: TestClient):
    """Test that search page contains mock results for a query."""
    query = "test"
    response = client.get(f"/search/?q={query}")

    assert response.status_code == 200
    assert f"Result 1 for &#39;{query}&#39;" in response.text
    assert f"Result 2 for &#39;{query}&#39;" in response.text


def test_search_page_without_query_has_no_results(client: TestClient):
    """Test that search page without query doesn't show results."""
    response = client.get("/search/")

    assert response.status_code == 200
    assert "Result 1 for" not in response.text
    assert "Result 2 for" not in response.text
