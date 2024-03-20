from django.shortcuts import render
from testapp.models import Student
from testapp.serializers import StudentSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import BasicAuthentication,SessionAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # authentication_classes = [BasicAuthentication,]
    authentication_classes = [SessionAuthentication,]
    permission_classes = [IsAuthenticated,]