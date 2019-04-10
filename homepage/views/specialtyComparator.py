from django.conf import settings
from django_mako_plus import view_function, jscontext
from datetime import datetime, timezone
from homepage import models as hmod
from django.contrib.auth.models import User
from django.db.models import Avg
import requests
from django import forms

@view_function
def process_request(request):

    if request.method == 'POST':
        form = PrescriberForm(request.POST)
        if form.is_valid():

            DoctorID = form.cleaned_data.get('DoctorID')

            url = "https://ussouthcentral.services.azureml.net/workspaces/1280ec3736a7452db2ad1b4ffdf4fee8/services/fe553bad406e451fa2dd3fb3995f32db/execute"

            querystring = {"api-version":"2.0","details":"true"}

            payload = "{\r\n  \"Inputs\": {\r\n    \"input1\": {\r\n      \"ColumnNames\": [\r\n        \"DoctorID\"\r\n      ],\r\n      \"Values\": [\r\n        [\r\n          \"" + DoctorID + "\"\r\n        ]\r\n      ]\r\n    }\r\n  }"
            headers = {
            'Authorization': "bearer 6rw7cCtENKlbnDEzAKtct4hEUrLrHNftvJICZEenbbSFaQg6ffP2OERsQ1Xp0ornbkdkebYzXPmJttqVqj4hQA==",
            'Content-Type': "application/json",
            'cache-control': "no-cache",
            'Postman-Token': "79695986-3c0e-4b62-a7ce-82217bd07a3b"
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

            # specialties = []
            # for i in range(len(valueList)):
            #     specialties += hmod.Doctor.objects.filter(DoctorID = int(valueList[i]))
            
        else:
            valueList = []
            
    else:
        form = PrescriberForm()  
        valueList = []      


    context = {
        'form': form,
        'valueList': valueList,
    }

    return request.dmp.render('specialtyComparator.html', context)


class PrescriberForm(forms.Form):
    DoctorID = forms.CharField(label='Prescriber ID', max_length=100)
    
    def clean(self):
        if len(self.cleaned_data.get('DoctorID')) != 10: 
          raise forms.ValidationError("Please enter a valid DoctorID")
        return self.cleaned_data