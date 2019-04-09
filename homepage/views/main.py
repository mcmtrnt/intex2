from django.conf import settings
from django_mako_plus import view_function, jscontext
from datetime import datetime, timezone
from homepage import models as hmod
from django.contrib.auth.models import User
from django import forms


@view_function
def process_request(request): #give them defaults

            # prescribers = hmod.Prescriber.objects.all().filter(Fname__contains = param) | hmod.Prescriber.objects.all().filter(Lname__contains = param) | hmod.Prescriber.objects.all().filter(Gender__contains = param) | hmod.Prescriber.objects.all().filter(Credentials__contains = param) | hmod.Prescriber.objects.all().filter(State__contains = param) | hmod.Prescriber.objects.all().filter(Specialty__contains = param)
            # prescribers = prescribers[:100]
                
            # opioids = hmod.Opioids.objects.all()[:100]


    prescribers = hmod.Doctor.objects.all()[:100]
    opioids = hmod.Drug.objects.all()[:100]

    context = {
        'prescribers': prescribers,
        'opioids': opioids,
    }
    return request.dmp.render('main.html', context)


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

    return request.dmp.render('main.prescribers.html', context)


@view_function
def drugs(request, param):
    
    if param != None:
        opioids = hmod.Drug.objects.all().filter(DrugName__contains = param) | hmod.Drug.objects.all().filter(IsOpioid__contains = param)
        opioids = opioids[:100]
    else:
        opioids = hmod.Drug.objects.all()[:100]

    context = {
        'opioids': opioids,
    }

    return request.dmp.render('main.drugs.html', context)