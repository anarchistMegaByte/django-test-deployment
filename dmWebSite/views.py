from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import requests  
import json

# Create your views here.
@csrf_exempt
def saveUserInfo(request):
    if request.method == 'POST':
        received_json_data=json.loads(request.body)
        answer = received_json_data['user_name']
        return HttpResponse(answer)
    else:
        return HttpResponse("Hello World")

