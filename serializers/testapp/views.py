from urllib import request
from django.shortcuts import render
from django.views import View
from testapp.models import Student
from django.core.serializers import serialize
from django.http import HttpResponse
import json
from testapp.Mixins import SerializeMixin,HttpResponseMixin
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .utils import is_json

from testapp.forms import StudentForm
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
@method_decorator(csrf_exempt, name='dispatch')
class StudentListView(HttpResponseMixin,SerializeMixin,View):
    def get(self, request,*args, **kwargs):
        stu_data = Student.objects.all()
        json_data = self.serialize(stu_data)
        return HttpResponse(json_data, content_type='application/json')
    
    def post(self,request,*args, **kwargs):
        data = request.body
        valid_json = is_json(data)
        if not valid_json:
            json_data = json.dumps({'msg': 'Please send only valid JSON data'})
            return self.render_to_http_response(json_data,status=400)
        stu_data = json.loads(data)
        form = StudentForm(stu_data)
        if form.is_valid():
            form.save()
            json_data = json.dumps({'msg': 'Student added successfully'})
            return self.render_to_http_response(json_data)
        if form.errors:
            json_data = json.dumps(form.errors)
            return self.render_to_http_response(json_data,status=400)
        



@method_decorator(csrf_exempt, name='dispatch')
class StudentDetailView(HttpResponseMixin,SerializeMixin,View):
    def get_object_by_id(self,id):
        try:
            stu = Student.objects.get(id=id)
        except Student.DoesNotExist:
            stu = None
        return stu
    
    def get(self, request,id,*args, **kwargs):
        try:
            stu = Student.objects.get(id=id)
        except Student.DoesNotExist:
            json_data = json.dumps({'msg': 'Student not found'})
            return self.render_to_http_response(json_data,status=404)
        else:
            json_data = self.serialize([stu,])
            return HttpResponse(json_data, content_type='application/json')
        
    def put(self,request,id,*args,**kwargs):
        stu = self.get_object_by_id(id)

        if stu is None:
            json_data = json.dumps({'msg': 'Student not found'})
            return self.render_to_http_response(json_data,status=404)
        
        data = request.body
        valid_json = is_json(data)
        
        if not valid_json:
            json_data = json.dumps({'msg': 'Please send only valid JSON data'})
            return self.render_to_http_response(json_data,status=400)
        
        provided_data = json.loads(data)
        original_data = {
            'name': stu.name,
            'roll': stu.roll,
            'address': stu.address,
        }
        original_data.update(provided_data)
        form = StudentForm(original_data,instance=stu)

        if form.is_valid():
            form.save()
            json_data = json.dumps({'msg': 'Student updated successfully'})
            return self.render_to_http_response(json_data)
        if form.errors:
            json_data = json.dumps(form.errors)
            return self.render_to_http_response(json_data,status=400)
    
    # delete
    def delete(self,request,id,*args,**kwargs):
        stu = self.get_object_by_id(id)
        if stu is None:
            json_data = json.dumps({'msg': 'Student not found unable to delete'})
            return self.render_to_http_response(json_data,status=404)
        status,delete_item = stu.delete()
        if status == 1:
            print(delete_item)
            json_data = json.dumps({'msg': 'Student deleted successfully'})
            return self.render_to_http_response(json_data,status=200)
        json_data = json.dumps({'msg': 'Unable to delete Plz try again'})
        return self.render_to_http_response(json_data,status=400)