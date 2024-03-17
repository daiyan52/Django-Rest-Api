from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from testapp.models import Student
from testapp.serializers import StudentSerializer
from testapp.pagination import myPagination
 
class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all().order_by('id')
    serializer_class = StudentSerializer
    # pagination_class = myPagination
 