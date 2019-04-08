from django.conf import settings
from django_mako_plus import view_function, jscontext
from datetime import datetime, timezone
from homepage import models as hmod
from django.contrib.auth.models import User
from django import forms


@view_function
def process_request(request):
    if request.method == 'POST':
        form = PrescriberForm(request.POST)
        if form.is_valid():
            # user = authenticate(username=form.cleaned_data.get('login'), password=form.cleaned_data.get('password'))
            # login(request, user)
            return HttpResponseRedirect('/homepage/editPrescribers/') #redirect to homepage
    else:
        form = PrescriberForm()

    return request.dmp.render('editPrescribers.html', {'form': form})


class PrescriberForm(forms.Form):
    DoctorID = forms.CharField(label='DoctorID', max_length=100)
    Fname = forms.CharField(label='First Name', max_length=100)
    Lname = forms.CharField(label='Last Name', max_length=100)
    Gender = forms.CharField(label='Gender', max_length=100)
    #State = forms.CharField(label='State', max_length=100)
    #Credentials = forms.CharField(label='Credentials', max_length=100)
    Specialty = forms.CharField(label='Specialty', max_length=100)
    OpioidPrescriber = forms.CharField(label='Opiod Prescriber', max_length=100)
    TotalPrescriptions = forms.CharField(label='Total Prescriptions', max_length=100)
    
    def clean(self):
        print("clean")
        # user = authenticate(username=self.cleaned_data.get('login'), password=self.cleaned_data.get('password'))
        # if user is None:
        #     raise forms.ValidationError("Your username or password is incorrect")
        # return self.cleaned_data