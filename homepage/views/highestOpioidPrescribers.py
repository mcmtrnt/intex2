from django.conf import settings
from django_mako_plus import view_function, jscontext
from datetime import datetime, timezone
from homepage import models as hmod
from django.contrib.auth.models import User
from django.db.models import Avg
import requests

@view_function
def process_request(request):
    
    highest = hmod.ExtraInfo.objects.all().order_by('-NumOpioids')[:20]

    context = {
        'highest': highest,
    }

    return request.dmp.render('highestOpioidPrescribers.html', context)