from django.conf import settings
from django_mako_plus import view_function, jscontext
from datetime import datetime, timezone
from homepage import models as hmod
from django.contrib.auth.models import User
from django.db.models import Avg
import http.client
import requests



@view_function
def process_request(request, DoctorID):

    prescriber = hmod.Doctor.objects.get(DoctorID = DoctorID)

    extra = hmod.ExtraInfo.objects.get(DoctorID = DoctorID)

    drugs = hmod.DrugDoctor.objects.filter(DoctorID = prescriber.DoctorID)

    mydrugs = []
    drugAvg = []
    avgArray = []

    for item in drugs:
        mydrugs += hmod.Drug.objects.filter(DrugName = item.DrugName)

        avg = hmod.DrugDoctor.objects.filter(DrugName = item.DrugName).aggregate(Avg('Qty'))

        drugAvg.append(str(round(avg.get('Qty__avg'), 2)))

        # for p in hmod.DrugDoctor.objects.raw('SELECT homepage_drugdoctor.DrugName, round(AVG(homepage_drugdoctor.Qty)) FROM intex.homepage_drugdoctor WHERE ' + item.DrugName + ' IN homepage_drugdoctor.DrugName'):
        #     print(p)

        # url = "https://ussouthcentral.services.azureml.net/workspaces/1280ec3736a7452db2ad1b4ffdf4fee8/services/8ae2f6f36e054367804466a761635e9b/execute"

        # querystring = {"api-version":"2.0","details":"true"}

        # payload = "{\r\n  \"Inputs\": {\r\n    \"input1\": {\r\n      \"ColumnNames\": [\r\n        \"Drug\"\r\n      ],\r\n      \"Values\": [\r\n        [\r\n          \"" + item.DrugName + "\"\r\n        ]\r\n      ]\r\n    }\r\n  }"
        # headers = {
        # 'Authorization': "bearer kiolgaq8+MqRa3HcihEwgpfZH08vH97G42L9KVwmg89pmGqN8iVgFq9/ud4r5GlGbpNvyivDQ5OmO0ObyHHdew==",
        # 'Content-Type': "application/json",
        # 'cache-control': "no-cache",
        # 'Postman-Token': "7ec9f02f-c398-43bd-9943-604962eb7e06"
        # }

        # response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

        # start = str(response.text).find('Values":[["')
        # s = str(response.text)[start:]            
        # end = str(response.text).find(']]')
        # values = str(response.text)[start + 11 : end - 1]
        # values = values.replace("\"", "")
        # valueList = values.split(',')
 
        # drugAvg.append(str(valueList[1]))
    print(drugAvg)
    print(drugAvg[0])
    context = {
        'prescriber': prescriber,
        'drugs': drugs,
        'mydrugs': mydrugs,
        'drugAvg': drugAvg,
        'extra': extra, 
    }
    return request.dmp.render('prescriberDetails.html', context)



@view_function
def related(request, param):

    url = "https://ussouthcentral.services.azureml.net/workspaces/1280ec3736a7452db2ad1b4ffdf4fee8/services/65de22ff44dc4bf6b1e56d55b5236af6/execute"

    querystring = {"api-version":"2.0","details":"true"}

    payload = "{\r\n  \"Inputs\": {\r\n    \"input1\": {\r\n      \"ColumnNames\": [\r\n        \"DoctorID\"\r\n      ],\r\n      \"Values\": [\r\n        [\r\n          \"" + param + "\"\r\n        ]\r\n      ]\r\n    }\r\n  }\r\n"
    headers = {
    'Authorization': "bearer p6rA25eaE9Z2f8TP420AoZWdWTZm8DcRvGv919hSQr7gz/PyCE+vxYgcc3EE0WInMf7FPKmke3qsLoEdpzOEyA==",
    'Content-Type': "application/json",
    'cache-control': "no-cache",
    'Postman-Token': "17067474-0e96-4020-8136-23fa599efe21"
    }

    response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

    print(response.text)

    start = str(response.text).find('Values":[["')
    s = str(response.text)[start:]            
    end = str(response.text).find(']]')
    values = str(response.text)[start + 11 : end - 1]
    values = values.replace("\"", "")
    valueList = values.split(',')

    doctors = []
    for i in range(len(valueList)):
        doctors += hmod.Doctor.objects.filter(DoctorID = int(valueList[i]))

    context = {
        'doctors': doctors,
    }

    return request.dmp.render('prescriberDetails.related.html', context)