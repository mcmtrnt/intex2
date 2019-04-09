from django.conf import settings
from django_mako_plus import view_function, jscontext
from datetime import datetime, timezone
from homepage import models as hmod
from django.contrib.auth.models import User
from django.contrib.auth import models as pmod


@view_function
def process_request(request):

    # g1 = pmod.Group()
    # # g1.name = "Data Clerks"
    # # g1.save()

    # g1= pmod.Group.objects.get(name='Data Clerks')
    # g1.permissions.add(pmod.Permission.objects.get(codename='view_drug'))
    # g1.permissions.add(pmod.Permission.objects.get(codename='view_doctor'))
    # g1.permissions.add(pmod.Permission.objects.get(codename='can_search'))
    # g1.permissions.add(pmod.Permission.objects.get(codename='change_user'))

    # p = pmod.Permission()
    # p.codename='view_analytics'
    # p.name='can view analytics'
    # p.content_type=pmod.Permission.objects.get(codename='add_user').content_type
    # p.save()

    # for p in pmod.Permission.objects.all():
    #     print(p)

    # user = User.objects.create_user(first_name = 'Andrew', last_name = 'Keeley', username='andrew',
    #                              email='test@test.com',
    #                              password='password')

    # user.groups.add(pmod.Group.objects.get(name='Prescribers'))

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