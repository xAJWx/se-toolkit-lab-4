"""End-to-end tests for the GET /interactions endpoint."""

import httpx


def test_get_interactions_returns_200(client: httpx.Client) -> None:
    """Test that GET /interactions/ returns 200 OK status code."""
    response = client.get("/interactions/")
    assert response.status_code == 200


def test_get_interactions_response_is_a_list(client: httpx.Client) -> None:
    """Test that GET /interactions/ response body is a JSON array."""
    response = client.get("/interactions/")
    data = response.json()
    assert isinstance(data, list)


def test_get_interactions_response_structure(client: httpx.Client) -> None:
    """Test that GET /interactions/ response has correct fields."""
    response = client.get("/interactions/")
    data = response.json()
    
    # Проверяем, что это список
    assert isinstance(data, list)
    
    # Если есть данные, проверяем структуру первого элемента
    if len(data) > 0:
        first = data[0]
        expected_fields = {"id", "learner_id", "item_id", "kind", "created_at"}
        assert expected_fields.issubset(first.keys()), f"Missing fields: {expected_fields - first.keys()}"