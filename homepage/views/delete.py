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
    doctor.delete()
    
    #     roberto = hmod.Doctor.objects.filter(DoctorID = '1992994776')
    # roberto[0].delete()
    
    context = {

    }

    return request.dmp.render('confirmation.html', context)