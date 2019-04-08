from django.conf import settings
from django_mako_plus import view_function, jscontext
from datetime import datetime, timezone
from homepage import models as hmod
from django.contrib.auth.models import User


@view_function
def process_request(request):
    # user = User.objects.create_user(first_name = 'Trent', last_name = 'McMillan', username='trent',
    #                              email='test@test.com',
    #                              password='password')
    # user.save()
    # u = User()
    # u.first_name = 'Trent'
    # u.last_name = 'McMillan'
    # u.email = 'test@test.com'
    # u.username = 'myusername'
    # u.set_password('password')
    # u.save()
    context = {

    }
    return request.dmp.render('index.html', context)