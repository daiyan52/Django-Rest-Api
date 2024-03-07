from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from testapp.models import Employee
from django.views import View
import json
from django.core.serializers import serialize
# Create your views here.

class EmployeeView(View):
    def get(self, request,id,*args, **kwargs):
        emp = Employee.objects.get(id=id)
        # emp_data ={
        #     'ename':emp.ename,
        #     'esal':emp.esal,
        #     'eaddress': emp.eaddress,
        # }
        
        emp_json = serialize('json',[emp,])
        return HttpResponse(emp_json, content_type='application/json')
        # return JsonResponse(emp_data)
