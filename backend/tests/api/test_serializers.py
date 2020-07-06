from api.serializers import RunSerializer
from decimal import *
import datetime

def test_valid_run():
    valid_serializer_data = {
        'total_time': datetime.timedelta(seconds=1395),
        'total_distance': Decimal('3.15'),
        'date': datetime.date(2020, 7, 6)
    }
    serializer = RunSerializer(data=valid_serializer_data)
    assert serializer.is_valid(raise_exception=True)
    assert serializer.validated_data == valid_serializer_data
    # assert serializer.data == valid_serializer_data
    assert serializer.errors == {}