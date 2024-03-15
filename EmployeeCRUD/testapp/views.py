from django.shortcuts import render
from testapp.serializers import EmployeeSerializer
from testapp.models import Employee
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class EmployeeCRUD(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    authentication_classes = [TokenAuthentication,]
    permission_classes = [IsAuthenticated,]
