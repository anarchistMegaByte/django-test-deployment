from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import requests  
import json

# Create your views here.
@csrf_excempt
def saveUserInfo(request):
    if request.method == 'POST':
        received_json_data=json.loads(request.body)
        return HttpResponse(received_json_data)
    else:
        return HttpResponse("Hello World")

