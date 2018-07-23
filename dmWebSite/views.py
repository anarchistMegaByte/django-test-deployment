from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from dmWebSite.models import dmWebsiteUser
import requests  
import json

# Create your views here.
@csrf_exempt
def saveUserInfo(request):
    if request.method == 'POST':
        received_json_data=json.loads(request.body)
        u1 = dmWebsiteUser(user_name=received_json_data['user_name'], user_email=received_json_data['user_email'], user_phone=received_json_data['user_phone'])
        u1.save()
        return HttpResponse(answer)
    else:
        return HttpResponse("Hello World")

