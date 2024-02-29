from django.shortcuts import render
from django.views import View
from testapp.models import Student
from django.core.serializers import serialize
from django.http import HttpResponse
import json
from testapp.Mixins import SerializeMixin
# Create your views here.
# class StudentView(View):
#     def get(self, request,*args, **kwargs):
#         stu = Student.objects.all()
#         json_data = serialize('json',stu,)
#         p_dict = json.loads(json_data)
#         final_list = []
#         for obj in p_dict:
#             stu_data = obj['fields']
#             final_list.append(stu_data)
#         final_data = json.dumps(final_list)
#         return HttpResponse(final_data, content_type='application/json')

class StudentListView(SerializeMixin,View):
    def get(self, request,*args, **kwargs):
        stu_data = Student.objects.all()
        json_data = self.serialize(stu_data)
        return HttpResponse(json_data, content_type='application/json')

class StudentDetailView(SerializeMixin,View):
    def get(self, request,id,*args, **kwargs):
        try:
            stu_data = Student.objects.get(id=id)
        except Student.DoesNotExist:
            return HttpResponse("Student does not exist")
        else:
            json_data = self.serialize(stu_data)
            return HttpResponse(json_data, content_type='application/json')
