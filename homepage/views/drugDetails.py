from django.conf import settings
from django_mako_plus import view_function, jscontext
from datetime import datetime, timezone
from homepage import models as hmod
from django.contrib.auth.models import User
import requests


@view_function
def process_request(request, id):

    drugs = hmod.Drug.objects.get(id = id)

    prescribers = hmod.DrugDoctor.objects.filter(DrugName = drugs.DrugName).order_by('-Qty')
    prescribers = prescribers[:10]

    myPrescribers = []
    for item in prescribers:
        myPrescribers += hmod.Doctor.objects.filter(DoctorID = item.DoctorID)


    context = {
        'drugs': drugs,
        'prescribers': prescribers,
        'myPrescribers': myPrescribers,
    }
    return request.dmp.render('drugDetails.html', context)


@view_function
def related(request, param):

    url = "https://ussouthcentral.services.azureml.net/workspaces/1280ec3736a7452db2ad1b4ffdf4fee8/services/776cadc691ae4d52b8f19c3fc5954206/execute"

    querystring = {"api-version":"2.0","details":"true"}

    payload = "{\r\n  \"Inputs\": {\r\n    \"input1\": {\r\n      \"ColumnNames\": [\r\n        \"DrugName\"\r\n      ],\r\n      \"Values\": [\r\n        [\r\n          \"ABILIFY\"\r\n        ]\r\n      ]\r\n    }\r\n  }"
    headers = {
    'Authorization': "bearer /G7bL1Tng63gSpGUjTCmeTa0LMewwpvAXQIx6dEFN3dCYqn1F3jElhSajEq91+jnPA/FHfJksw3aVEtEAuqKHQ==",
    'Content-Type': "application/json",
    'cache-control': "no-cache",
    'Postman-Token': "19c8484f-cf4d-471e-bc40-a4ad7b27f588"
    }

    response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

    start = str(response.text).find('Values":[["')
    s = str(response.text)[start:]            
    end = str(response.text).find(']]')
    values = str(response.text)[start + 11 : end - 1]
    values = values.replace("\"", "")
    valueList = values.split(',')

    drugs = []
    for i in range(len(valueList)):
        drugs += hmod.Drug.objects.filter(DrugName = str(valueList[i]))

    context = {
        'drugs':drugs,
    }

    return request.dmp.render('drugDetails.related.html', context)