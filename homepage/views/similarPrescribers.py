from django.conf import settings
from django_mako_plus import view_function, jscontext
from datetime import datetime, timezone
from homepage import models as hmod
from django.contrib.auth.models import User
from django.db.models import Avg
import requests
from django import forms
import json
from decimal import Decimal

@view_function
def process_request(request):

    if request.method == 'POST':
        form = PrescriberForm(request.POST)
        if form.is_valid():

            DoctorID = form.cleaned_data.get('DoctorID')

            url = "https://ussouthcentral.services.azureml.net/workspaces/1280ec3736a7452db2ad1b4ffdf4fee8/services/65de22ff44dc4bf6b1e56d55b5236af6/execute"

            querystring = {"api-version":"2.0","details":"true"}

            payload = "{\r\n  \"Inputs\": {\r\n    \"input1\": {\r\n      \"ColumnNames\": [\r\n        \"DoctorID\"\r\n      ],\r\n      \"Values\": [\r\n        [\r\n          \"" + DoctorID + "\"\r\n        ]\r\n      ]\r\n    }\r\n  }\r\n"
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
            print(valueList)

            doctors = []
            for i in range(len(valueList)):
                doctors += hmod.Doctor.objects.filter(DoctorID = int(valueList[i]))
            
            
    else:
        form = PrescriberForm()  
        doctors = []      


    context = {
        'form': form,
        'doctors': doctors,
    }

    return request.dmp.render('similarPrescribers.html', context)


class PrescriberForm(forms.Form):
    DoctorID = forms.CharField(label='DoctorID', max_length=100)
    
    def clean(self):
        return self.cleaned_data



