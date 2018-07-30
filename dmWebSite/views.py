from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from dmWebSite.models import dmWebsiteUser
from dmWebSite.models import dmWebsiteUserOnlyEmails
import requests  
import json

# Create your views here.
@csrf_exempt
def saveUserInfo(request):
    if request.method == 'POST':
        received_json_data=json.loads(request.body)
        u1 = dmWebsiteUser(user_name=received_json_data['user_name'], user_email=received_json_data['user_email'], user_phone=received_json_data['user_phone'])
        u1.save()
        return HttpResponse("Success!!")
    else:
        return HttpResponse("Not a POST request.")

@csrf_exempt
def saveUserEmail(request):
    if request.method == 'POST':
        received_json_data=json.loads(request.body)
        u1, created = dmWebsiteUserOnlyEmails.objects.get_or_create(
                            user_email=received_json_data['user_email']
                        )
        #u1 = dmWebsiteUserOnlyEmails(user_email=received_json_data['user_email'])
        u1.save()
        if created:
            return HttpResponse("Success!! Created : " + str(created))
        else:
            return HttpResponse("Success!! Entry already present")
    else:
        return HttpResponse("Error : Not a POST request.")

