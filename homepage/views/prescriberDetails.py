from django.conf import settings
from django_mako_plus import view_function, jscontext
from datetime import datetime, timezone
from homepage import models as hmod
from django.contrib.auth.models import User
from django.db.models import Avg
import http.client
# import socket



@view_function
def process_request(request, DoctorID):

    prescriber = hmod.Doctor.objects.get(DoctorID = DoctorID)

    drugs = hmod.DrugDoctor.objects.filter(DoctorID = prescriber.DoctorID)

    mydrugs = []
    drugAvg = []
    for item in drugs:
        mydrugs += hmod.Drug.objects.filter(DrugName = item.DrugName)

        drugAvg += hmod.DrugDoctor.objects.filter(DrugName = item.DrugName)


    # socket.getaddrinfo('localhost', 8080)
    # conn = http.client.HTTPConnection("ussouthcentral,services,azureml,net")

    # payload = "{\r\n  \"Inputs\": {\r\n    \"input1\": {\r\n      \"ColumnNames\": [\r\n        \"DoctorID\"\r\n      ],\r\n      \"Values\": [\r\n        [\r\n          \"1003002320\"\r\n        ]\r\n      ]\r\n    }\r\n  }\r\n"

    # headers = {
    # 'Authorization': "bearer p6rA25eaE9Z2f8TP420AoZWdWTZm8DcRvGv919hSQr7gz/PyCE+vxYgcc3EE0WInMf7FPKmke3qsLoEdpzOEyA==",
    # 'Content-Type': "application/json",
    # 'cache-control': "no-cache",
    # 'Postman-Token': "404c0a02-fbf6-4490-8df2-88c86fb60e59"
    # }

    # conn.request("POST", "workspaces,1280ec3736a7452db2ad1b4ffdf4fee8,services,65de22ff44dc4bf6b1e56d55b5236af6,execute", payload, headers)

    # res = conn.getresponse()
    # data = res.read()

    # print(data.decode("utf-8"))
 
    

    context = {
        'prescriber': prescriber,
        'drugs': drugs,
        'mydrugs': mydrugs,
        'drugAvg': drugAvg,
    }
    return request.dmp.render('prescriberDetails.html', context)