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
