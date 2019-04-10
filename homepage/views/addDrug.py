from django.conf import settings
from django_mako_plus import view_function, jscontext
from datetime import datetime, timezone
from homepage import models as hmod
from django.contrib.auth.models import User
from django import forms
from django.http import HttpResponseRedirect


@view_function
def process_request(request, id):
    doctor = hmod.Doctor.objects.get(DoctorID = id)

    if request.method == 'POST':
        form = DrugForm(request.POST)
        if form.is_valid():

            dd = hmod.DrugDoctor()
            dd.DoctorID = doctor.DoctorID  
            dd.DrugName = form.cleaned_data.get('DrugName')
            dd.Qty = form.cleaned_data.get('Qty')

            dd.save()

            return HttpResponseRedirect('/homepage/confirmation/') 
    else:
        form = DrugForm()

    context = {
        'form': form,
        'doctor': doctor,
    }

    return request.dmp.render('addDrug.html', context)



class DrugForm(forms.Form):
    DrugName = forms.CharField(label='Drug Name', max_length=100)
    Qty = forms.CharField(label='Quantity', max_length=100) 

    
    def clean(self):
        drug = hmod.Drug.objects.filter(DrugName = self.cleaned_data.get('DrugName'))

        if len(drug) <= 0:
            raise forms.ValidationError("Enter a valid drug name")

        if int(self.cleaned_data.get('Qty')) < 0: 
          raise forms.ValidationError("Please enter a valid quantity")
            

        return self.cleaned_data