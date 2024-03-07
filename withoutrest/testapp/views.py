from django.views import View
from django.shortcuts import render
from django.http import HttpResponse
import json

# Create your views here.
def studentView(request):
    studentData = {
        'name' :'Daiyan Alam',
        'roll' : 52,
        'address' :'Siwan,Bihar',
    }
    resp = '<h1>Name={}<br>Roll={}<br>Address={}<br></h1>'.format(
        studentData['name'], 
        studentData['roll'], 
        studentData['address'
        ])
    return HttpResponse(resp)

def studentJsonView(request):
    studentData = {
        'name' :'Daiyan Alam',
        'roll' : 52,
        'address' :'Siwan,Bihar',
    }
    resp = json.dumps(studentData)
    return HttpResponse(resp,content_type='application/json')

from django.http import JsonResponse
def studentJsonView2(request):
    studentData = {
        'name' :'Daiyan Alam',
        'roll' : 52,
        'address' :'Kolkata',
    }
    return JsonResponse(studentData)

class jsonCBV(View):
    def get(self, request,*args,**kwargs):
        studentData = {
            'name' :'Daiyan Alam',
            'roll' : 52,
            'address' :'Siwan,Bihar',
        }
        
        return JsonResponse(studentData)
    
from testapp.Mixins import HttpResponseMixin
class jsonCBV1(HttpResponseMixin,View):
    def get(self, request,*args,**kwargs):
        json_data = json.dumps({"msg":"i am from get"})
        return self.render_to_http_response(json_data)
    
    def put(self,request,*args,**kwargs):
        json_data = json.dumps({"msg":"i am from put"})
        return self.render_to_http_response(json_data)
    
    def post(self,request,*args,**kwargs):
        json_data = json.dumps({"msg":"i am from post"})
        return self.render_to_http_response(json_data)
    
    def delete(self,request,*args,**kwargs):
        json_data = json.dumps({"msg":"i am from delete"})
        return self.render_to_http_response(json_data)