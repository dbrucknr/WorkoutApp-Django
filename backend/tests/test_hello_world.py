import json

from django.urls import reverse

def test_hello_world():
    assert "hello_world" == "hello_world"

def test_data(client):
    url = reverse("data")
    response = client.get(url)
    content = json.loads(response.content)
    assert response.status_code == 200
    assert content["data"] == "packet"