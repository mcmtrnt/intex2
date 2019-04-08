from django.conf import settings
from django_mako_plus import view_function, jscontext
from datetime import datetime, timezone
from homepage import models as hmod
from django.contrib.auth.models import User


@view_function
def process_request(request, DoctorID):

    prescriber = hmod.Doctor.objects.get(DoctorID = DoctorID)

    drugs = hmod.DrugDoctor.objects.filter(DoctorID = prescriber.DoctorID)

    context = {
        'prescriber': prescriber,
        'drugs': drugs,
    }
    return request.dmp.render('prescriberDetails.html', context)