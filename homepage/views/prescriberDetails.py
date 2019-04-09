from django.conf import settings
from django_mako_plus import view_function, jscontext
from datetime import datetime, timezone
from homepage import models as hmod
from django.contrib.auth.models import User
from django.db.models import Avg
import http.client


@view_function
def process_request(request, DoctorID):

    prescriber = hmod.Doctor.objects.get(DoctorID = DoctorID)

    drugs = hmod.DrugDoctor.objects.filter(DoctorID = prescriber.DoctorID)

    mydrugs = []
    drugAvg = []
    for item in drugs:
        mydrugs += hmod.Drug.objects.filter(DrugName = item.DrugName)

        drugAvg += hmod.DrugDoctor.objects.filter(DrugName = item.DrugName)


   

    conn = http.client.HTTPConnection("ussouthcentral,services,azureml,net")

    payload = "{\r\n  \"Inputs\": {\r\n    \"Web input\": {\r\n      \"ColumnNames\": [\r\n        \"Gender\",\r\n        \"State\",\r\n        \"Credentials\",\r\n        \"Specialty\",\r\n        \"TotalPrescriptions\"\r\n      ],\r\n      \"Values\": [\r\n        [\r\n          \"value\",\r\n          \"value\",\r\n          \"value\",\r\n          \"value\",\r\n          \"0\"\r\n        ],\r\n        [\r\n          \"value\",\r\n          \"value\",\r\n          \"value\",\r\n          \"value\",\r\n          \"0\"\r\n        ]\r\n      ]\r\n    }\r\n  },\r\n  \"GlobalParameters\": {}\r\n}"

    headers = {
    'Authorization': "bearer o74oVphPyeiQPFgMzwpkm0k6AtgIqjWZQg1L9+myTJTgcLf+6WXSga7FRw+9myIYtwcvUZMlgqyn92MclBy4oA==",
    'Content-Type': "application/json",
    'cache-control': "no-cache",
    'Postman-Token': "ddb99f40-a943-4ae3-804d-8a3ed82641a5"
    }

    conn.request("POST", "workspaces,1280ec3736a7452db2ad1b4ffdf4fee8,services,904fb1ad86594947a63dd8ad9047933e,execute", payload, headers)

    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))

    

    context = {
        'prescriber': prescriber,
        'drugs': drugs,
        'mydrugs': mydrugs,
        'drugAvg': drugAvg,
    }
    return request.dmp.render('prescriberDetails.html', context)