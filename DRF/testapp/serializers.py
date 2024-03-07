from rest_framework import serializers

class EmployeeSerializer(serializers.Serializer):
    ename = serializers.CharField(max_length=25)
    esal = serializers.FloatField()
    eaddress = serializers.CharField(max_length=100)