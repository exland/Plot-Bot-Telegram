import os
import sys

import django
import datetime

"""Run administrative tasks."""
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()
#mark django settings module as settings.py
#os.environ.setdefault("DJANGO_SETTINGS_MODULE",'project.settings')
#instantiate a web sv for django which is a wsgi
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()


#import your models schema
from GraphBot.models import User



def DeleteUser(arg_id):
    result = User.objects.filter(id=arg_id)
    result.delete()



def UsersLookup(arg_id):
    result =  User.objects.filter(id=arg_id)
    print(list(result))
    if not result:
        return False
    return True


def CreateUser(arg_id, name_arg, time_span_arg):
    if len(name_arg) >= 30:
        return False
    user = User(id=arg_id,time_span= time_span_arg, name=name_arg,table_num = 0, selected_num=0)
    user.save()




def MeasurementLookup(arg_id):
    result = Measurement.objects.exclude(id=arg_id, date= datetime.datetime.now())

# #Create Operations here
# data_dict={'name':'Nimish','age':23}
# t= Teacher(**data_dict)
# t.save()

# # Read operation logic
# k = list(Teacher.objects.all().filter(age=23))

# print(k)
# #print(f'Hello, I am {t.name}, {t.age} y/o.')