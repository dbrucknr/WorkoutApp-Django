import pytest

from workouts.models import Run


@pytest.mark.django_db
def test_run_model():
    run = Run(
        total_time="00:23:15", 
        total_distance=3.15, 
        date="1987-01-01",
        )
    run.save()
    assert run.total_time=="00:23:15"
    assert run.total_distance==3.15
    assert run.date=="1987-01-01"