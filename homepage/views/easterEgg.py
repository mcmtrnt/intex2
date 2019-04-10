from django.conf import settings
from django_mako_plus import view_function, jscontext
from homepage import models as hmod
from django.contrib.auth.models import User


@view_function
def process_request(request):
    

    context = {

    }

    return request.dmp.render('easterEgg.html', context)