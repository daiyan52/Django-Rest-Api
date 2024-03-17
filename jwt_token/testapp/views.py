from django.shortcuts import render
from testapp.serializers import StudentSerializer
from rest_framework.viewsets import ModelViewSet
from testapp.models import Student
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
# Create your views here.

class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [JWTAuthentication,]
    permission_classes = [IsAuthenticated,]