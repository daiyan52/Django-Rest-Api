from django.shortcuts import render
from testapp.models import Employee
from django.http import HttpResponse
from django.views import View
from testapp.Mixins import SerializeMixin,HttpResponseMixin
import json
from testapp.utils import is_json
class EmployeeView(HttpResponseMixin,SerializeMixin,View):
    def get_by_id(self, id):
        try:
            emp = Employee.objects.get(id=id)
        except:
            emp = None
        return emp

    def get(self, request,*args, **kwargs):
        data = request.body

        valid_json = is_json(data)

        if not valid_json:
            return self.render_to_http_response(json.dumps({'msg': 'Invalid JSON'}), status=400)
        
        pdata = json.loads(data)

        id = pdata.get('id',None)

        if id is not None:
            emp = self.get_by_id(id)
            if emp is None:
                json_data = json.dumps({'msg': 'Employee not found'})
                return self.render_to_http_response(json_data,status=404)
            else:
                json_data = json.dumps(emp)
                return self.render_to_http_response(json_data)