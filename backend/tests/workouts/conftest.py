import pytest
from workouts.models import Run  

@pytest.fixture(scope='function')
def add_run():
    def _add_run(total_time, total_distance, date):
        run = Run.objects.create(total_time=total_time, total_distance=total_distance, date=date)
        return run
    return _add_run