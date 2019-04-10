from django.conf import settings
from django_mako_plus import view_function, jscontext
from datetime import datetime, timezone
from homepage import models as hmod
from django.contrib.auth.models import User
from django import forms
from django.http import HttpResponseRedirect


@view_function
def process_request(request): #default = None?
    prescribers = hmod.Doctor.objects.all().order_by('-DoctorID')[:100]

    if request.method == 'POST':
        form = PrescriberForm(request.POST)
        if form.is_valid():

            p = hmod.Doctor()
            p.DoctorID = prescribers[0].DoctorID + 1
            p.Fname = form.cleaned_data.get('Fname')
            p.Lname = form.cleaned_data.get('Lname')
            p.Gender = form.cleaned_data.get('Gender')
            p.State = form.cleaned_data.get('State')
            p.Credentials = form.cleaned_data.get('Credentials')
            p.Specialty = form.cleaned_data.get('Specialty')
            p.OpioidPrescriber = form.cleaned_data.get('OpioidPrescriber')
            p.TotalPrescriptions = form.cleaned_data.get('TotalPrescriptions')

            p.save()

            return HttpResponseRedirect('/homepage/confirmation/') #redirect to a receipt type page.
    else:
        form = PrescriberForm()

    context = {
        'form': form,
        'prescribers': prescribers,
    }

    return request.dmp.render('editPrescribers.html', context)


class PrescriberForm(forms.Form):
    #DoctorID = forms.CharField(label='DoctorID', max_length=100)
    Fname = forms.CharField(label='First Name', max_length=100)
    Lname = forms.CharField(label='Last Name', max_length=100)
    Gender = forms.CharField(label='Gender', max_length=100)
    State = forms.CharField(label='State (ex. UT)', max_length=100)
    Credentials = forms.CharField(label='Credentials', max_length=100)
    Specialty = forms.CharField(label='Specialty', max_length=100)
    OpioidPrescriber = forms.CharField(label='Opiod Prescriber (1 or 0)', max_length=100)
    TotalPrescriptions = forms.CharField(label='Total Prescriptions', max_length=100)

    
    def clean(self):
        if self.cleaned_data.get('OpioidPrescriber') != '0' and self.cleaned_data.get('OpioidPrescriber') != '1': 
            raise forms.ValidationError("Enter a 1 or 0")

        if self.cleaned_data.get('Gender') != 'M' and self.cleaned_data.get('Gender') != 'F': 
          raise forms.ValidationError("Please enter gender as M or F")

        if len(self.cleaned_data.get('State')) > 3: 
          raise forms.ValidationError("Please enter a state abbreviation")

        if int(self.cleaned_data.get('TotalPrescriptions')) < 0: 
          raise forms.ValidationError("Please enter a valid number of Total Prescriptions")
          
        return self.cleaned_data


@view_function
def prescribers(request, param):

    if param != None:
        prescribers = hmod.Doctor.objects.all().filter(Fname__contains = param) | hmod.Doctor.objects.all().filter(Lname__contains = param) | hmod.Doctor.objects.all().filter(Gender__contains = param) | hmod.Doctor.objects.all().filter(Credentials__contains = param) | hmod.Doctor.objects.all().filter(State__contains = param) | hmod.Doctor.objects.all().filter(Specialty__contains = param)
        prescribers = prescribers[:100]
    else:
        prescribers = hmod.Doctor.objects.all()[:100]

    context = {
        'prescribers': prescribers,
    }

    return request.dmp.render('editPrescribers.prescribers.html', context)