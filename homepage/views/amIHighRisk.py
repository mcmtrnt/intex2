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

            gender = form.cleaned_data.get('Gender')
            state = form.cleaned_data.get('State')
            credentials = form.cleaned_data.get('Credentials')
            specialty = form.cleaned_data.get('Specialty')
            totalPrescriptions = form.cleaned_data.get('TotalPrescriptions')


            url = "https://ussouthcentral.services.azureml.net/workspaces/1280ec3736a7452db2ad1b4ffdf4fee8/services/904fb1ad86594947a63dd8ad9047933e/execute"

            querystring = {"api-version":"2.0","details":"true"}

            payload = "{\r\n  \"Inputs\": {\r\n    \"Web input\": {\r\n      \"ColumnNames\": [\r\n        \"Gender\",\r\n        \"State\",\r\n        \"Credentials\",\r\n        \"Specialty\",\r\n        \"TotalPrescriptions\"\r\n      ],\r\n      \"Values\": [\r\n        [\r\n          \"" + gender + "\",\r\n          \"" + state + "\",\r\n          \"" + credentials + "\",\r\n          \"" + specialty + "\",\r\n          \""+ totalPrescriptions +"\"\r\n        ]\r\n      ]\r\n    }\r\n  }"
            headers = {
            'Authorization': "bearer o74oVphPyeiQPFgMzwpkm0k6AtgIqjWZQg1L9+myTJTgcLf+6WXSga7FRw+9myIYtwcvUZMlgqyn92MclBy4oA==",
            'Content-Type': "application/json",
            'cache-control': "no-cache",
            'Postman-Token': "27290ef0-98ba-41d6-8a4f-2389a1417b8f"
            }

            response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

            start = str(response.text).find('Values":[["0')
            s = str(response.text)[start:]            
            end = str(response.text).find(']]')
            values = str(response.text)[start + 11 : end - 1]
            values = values.replace("\"", "")
            valueList = values.split(',')
            
            chance = valueList[1]
            chance = Decimal(chance) * 100
            chance = round(chance, 2)

            atRisk = valueList[2]
            if atRisk == '0':
                atRisk = 'No'
            else:
                atRisk = 'Yes'
        else:      
            chance = ""
            atRisk = ""
            
    else:
        form = PrescriberForm()        
        chance = ""
        atRisk = ""

    context = {
        'form': form,
        'chance': chance,
        'atRisk': atRisk,
    }

    return request.dmp.render('amIHighRisk.html', context)


class PrescriberForm(forms.Form):
    Gender = forms.CharField(label='Gender (M/F)', max_length=100)
    State = forms.CharField(label='State (ex. UT)', max_length=100)
    Credentials = forms.CharField(label='Credentials', max_length=100)
    Specialty = forms.CharField(label='Specialty', max_length=100)
    TotalPrescriptions = forms.CharField(label='Total Prescriptions', max_length=100)

    
    def clean(self):
        if self.cleaned_data.get('Gender') != 'M' and self.cleaned_data.get('Gender') != 'F': 
          raise forms.ValidationError("Please enter gender as M or F")

        if len(self.cleaned_data.get('State')) > 3: 
          raise forms.ValidationError("Please enter a state abbreviation")

        if int(self.cleaned_data.get('TotalPrescriptions')) < 0: 
          raise forms.ValidationError("Please enter a valid number of Total Prescriptions")

        return self.cleaned_data