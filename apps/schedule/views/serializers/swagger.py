from rest_framework import serializers


# Main Section
class ScheduleSwaggerSerializer(serializers.Serializer):
    start_time = serializers.DateTimeField()
    end_time = serializers.DateTimeField()
    available_applicant_count = serializers.IntegerField()
