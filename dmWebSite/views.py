from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def saveUserInfo(request):
    return HttpResponse("Hello world")
    #if request.method == 'POST':

