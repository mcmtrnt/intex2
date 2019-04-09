from django.conf import settings
from django_mako_plus import view_function, jscontext
from datetime import datetime, timezone
from homepage import models as hmod
from django.contrib.auth.models import User


@view_function
def process_request(request, id):

    drugs = hmod.Drug.objects.get(id = id)

    prescribers = hmod.DrugDoctor.objects.filter(DrugName = drugs.DrugName).order_by('-Qty')
    prescribers = prescribers[:10]

    myPrescribers = []
    for item in prescribers:
        myPrescribers += hmod.Doctor.objects.filter(DoctorID = item.DoctorID)


    context = {
        'drugs': drugs,
        'prescribers': prescribers,
        'myPrescribers': myPrescribers,
    }
    return request.dmp.render('drugDetails.html', context)