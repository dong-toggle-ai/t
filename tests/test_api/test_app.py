def test_get_health(api_client):
    response = api_client.get("/health-check")
    assert response.status_code == 200
    assert response.text == "ok"
