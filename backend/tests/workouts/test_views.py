import json
import pytest
from workouts.models import Run

@pytest.mark.django_db
def test_add_run(client):
    runs = Run.objects.all()
    assert len(runs) == 0

    response = client.post(
        '/api/workouts/runs/',
        {
            "total_time":"00:23:15", 
            "total_distance":3.15, 
            "date":"1987-01-01"
        },
        content_type="application/json"
        )
    assert response.status_code == 201
    assert response.data["total_time"] == "00:23:15"

    runs = Run.objects.all()
    assert len(runs) == 1

@pytest.mark.django_db
def test_add_run_invalid_json(client):
    runs = Run.objects.all()
    assert len(runs) == 0

    resp = client.post(
        "/api/workouts/runs/",
        {},
        content_type="application/json"
    )
    assert resp.status_code == 400

    runs = Run.objects.all()
    assert len(runs) == 0

@pytest.mark.django_db
def test_add_run_invalid_json_keys(client):
    runs = Run.objects.all()
    assert len(runs) == 0

    resp = client.post(
        "/api/workouts/runs/",
        {
            "total_time":"00:23:15", 
            "total_distance":3.15, 
        },
        content_type="application/json"
    )
    assert resp.status_code == 400

    runs = Run.objects.all()
    assert len(runs) == 0

@pytest.mark.django_db
def test_get_single_run(client, add_run):
    run = add_run(
        total_time="00:23:15", 
        total_distance=3.15, 
        date="1987-01-01",
        )
    response = client.get(f"/api/workouts/runs/{run.id}/")
    assert response.status_code == 200
    assert response.data["total_time"] == "00:23:15"

def test_get_single_movie_incorrect_id(client):
    response = client.get(f"/api/workouts/runs/foo")
    assert response.status_code == 404

@pytest.mark.django_db
def test_get_all_runs(client, add_run):
    run_one = add_run(total_time="00:23:20", total_distance=3.2, date="2020-07-09")
    run_two = add_run(total_time="00:21:15", total_distance=3.11, date="2020-07-10")
    response = client.get("/api/workouts/runs/")
    assert response.status_code == 200
    assert response.data[0]["total_time"] == run_one.total_time
    assert response.data[1]["total_time"] == run_two.total_time