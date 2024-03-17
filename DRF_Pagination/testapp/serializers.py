from testapp.models import Student
from rest_framework.serializers import ModelSerializer

class StudentSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'