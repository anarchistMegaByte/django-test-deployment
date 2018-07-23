from django.shortcuts import render
from django.http import HttpResponse
import requests  
import json

# Create your views here.
def saveUserInfo(request):
    if request.method == 'POST':
        received_json_data=json.loads(request.body)
        return HttpResponse(received_json_data)

