from rest_framework import serializers
from workouts.models import Run

class RunSerializer(serializers.ModelSerializer):
    class Meta:
        model = Run
        fields = '__all__'
        # read_only_fields = ('total_time', 'total_distance', 'date',)