from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from dmWebSite.models import dmWebsiteUser
from dmWebSite.models import dmWebsiteUserOnlyEmails
from dmWebSite.models import dmWebsiteContactUs,dmWebsiteSubmitProjectDetails

import requests  
import json
from datetime import date,datetime
from utils.classifier import construct_net, predict_class_new
from utils.main import main_func
import numpy as np
import tensorflow as tf

# Create your views here.
@csrf_exempt
def saveUserInfo(request):
    if request.method == 'POST':
        received_json_data=json.loads(request.body)
        u1, created = dmWebsiteUser.objects.get_or_create(
                            user_name=received_json_data['user_name'], 
                            user_email=received_json_data['user_email'], 
                            user_phone=received_json_data['user_phone']
                        )
        # u1 = dmWebsiteUser(user_name=received_json_data['user_name'], user_email=received_json_data['user_email'], user_phone=received_json_data['user_phone'])
        u1.sts = datetime.today()
        u1.save()
        if created:
            return HttpResponse("Success!! Created : " + str(created))
        else:
            return HttpResponse("Success!! Entry already present")
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
        u1.sts = datetime.today()
        u1.save()
        if created:
            return HttpResponse("Success!! Created : " + str(created))
        else:
            return HttpResponse("Success!! Entry already present")
    else:
        return HttpResponse("Error : Not a POST request.")

@csrf_exempt
def saveContactUsInfo(request):
    if request.method == 'POST':
        received_json_data=json.loads(request.body)
        u1, created = dmWebsiteContactUs.objects.get_or_create( 
                            user_email=received_json_data['user_email']
                        )
        u1.user_first_name = received_json_data['user_first_name']
        u1.user_last_name = received_json_data['user_last_name']
        u1.user_message = received_json_data['user_message']
        # u1 = dmWebsiteUser(user_name=received_json_data['user_name'], user_email=received_json_data['user_email'], user_phone=received_json_data['user_phone'])
        u1.sts = datetime.today()
        u1.save()
        if created:
            return HttpResponse("Success!! Created : " + str(created))
        else:
            return HttpResponse("Success!! Entry already present")
    else:
        return HttpResponse("Not a POST request.")

@csrf_exempt
def saveProjectDetails(request):
    if request.method == 'POST':
        received_json_data=json.loads(request.body)
        u1, created = dmWebsiteSubmitProjectDetails.objects.get_or_create( 
                            user_email=received_json_data['user_email'],
                            user_phone_number=received_json_data['user_phone_number']
                        )
        u1.user_name = received_json_data['user_name']
        u1.user_institution = received_json_data['user_institution']
        u1.user_domain = received_json_data['user_domain']
        u1.user_project_title = received_json_data['user_project_title']
        u1.user_project_description = received_json_data['user_project_description']
        u1.sts = datetime.today()
        # u1 = dmWebsiteUser(user_name=received_json_data['user_name'], user_email=received_json_data['user_email'], user_phone=received_json_data['user_phone'])
        u1.sts = datetime.today()
        u1.save()
        if created:
            return HttpResponse("Success!! Created : " + str(created))
        else:
            return HttpResponse("Success!! Entry already present")
    else:
        return HttpResponse("Not a POST request.")


# clump_thickness: 0
# unif_cell_size: 1
# unif_cell_shape: 2
# marg_adhesion: 3
# single_epith_cell_size: 4
# bare_nuclei: 5
# bland_chrom: 6
# norm_nucleoli: 7
# mitoses: 8
@csrf_exempt
def get_cancer_results(request):
    if request.method == 'POST':
        tf.reset_default_graph()
        received_json_data=json.loads(request.body)
        model_dir = 'nn_classifier'
        dnn_model = construct_net(num_features=9, model_dir=model_dir)
        ori_arr = []
        ori_arr.append(received_json_data['clump_thickness'])
        ori_arr.append(received_json_data['unif_cell_size'])
        ori_arr.append(received_json_data['unif_cell_shape'])
        ori_arr.append(received_json_data['marg_adhesion'])
        ori_arr.append(received_json_data['single_epith_cell_size'])
        ori_arr.append(received_json_data['bare_nuclei'])
        ori_arr.append(received_json_data['bland_chrom'])
        ori_arr.append(received_json_data['norm_nucleoli'])
        ori_arr.append(received_json_data['mitoses'])
        x = np.array([ori_arr], dtype=np.float32)
        print(x)
        name = predict_class_new(dnn_model, {0: 'benign', 1: 'malignant'}, x)
        
        return HttpResponse(name)
    else:
        model_dir = 'nn_classifier'
        dnn_model = construct_net(num_features=9, model_dir=model_dir)
        manav = np.array([np.random.randint(11, size=9)], dtype=np.float32)
    
        #predict_class(dnn_model, {0: 'benign', 1: 'malignant'})
        name = predict_class_new(dnn_model, {0: 'benign', 1: 'malignant'}, manav)
        return HttpResponse(name)

@csrf_exempt
def start_training(request):
    if request.method == 'GET':
        main_func()
        
        return HttpResponse("Success!! Created")
        
        
    else:
        return HttpResponse("Error : Not a GET request.")
