from django.conf import settings
from django_mako_plus import view_function, jscontext
from datetime import datetime, timezone
from homepage import models as hmod
from django.contrib.auth.models import User
from django import forms
from django.http import HttpResponseRedirect


@view_function
def process_request(request, DoctorID, DrugName):

    doctor = hmod.Doctor.objects.get(DoctorID = DoctorID)
    drugDoctor = hmod.DrugDoctor.objects.get(DoctorID = DoctorID, DrugName = DrugName)

    if request.method == 'POST':
        form = DrugForm(request.POST)
        if form.is_valid():

            p = drugDoctor
            p.Qty = form.cleaned_data.get('Qty')

            p.save()

            return HttpResponseRedirect('/homepage/confirmation/') #redirect to a receipt type page.
    else:
        form = DrugForm()

    context = {
        'form': form,
        'doctor': doctor,
        'DrugName': DrugName,
        'drugDoctor': drugDoctor,
    }

    return request.dmp.render('editDrug.html', context)



class DrugForm(forms.Form):
    #DrugName = forms.CharField(label='Drug Name', max_length=100)
    Qty = forms.CharField(label='Quantity', max_length=100) #integer field?

    
    def clean(self):
        # drug = hmod.Drug.objects.filter(DrugName = self.cleaned_data.get('DrugName'))
         
        # if len(drug) <= 0:
        #     raise forms.ValidationError("Enter a valid drug name")

        if int(self.cleaned_data.get('Qty')) < 0: 
          raise forms.ValidationError("Please enter a valid quantity")
            

        return self.cleaned_data