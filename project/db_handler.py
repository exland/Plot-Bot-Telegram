import os
import sys

import django

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





def UsersLookup(arg_id):
    result =  User.objects.filter(id=arg_id)
    if not result:
        return False
    return True


# #Create Operations here
# data_dict={'name':'Nimish','age':23}
# t= Teacher(**data_dict)
# t.save()

# # Read operation logic
# k = list(Teacher.objects.all().filter(age=23))

# print(k)
# #print(f'Hello, I am {t.name}, {t.age} y/o.')