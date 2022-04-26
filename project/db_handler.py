import os
import sys

import django
import datetime
from enums import UserInput

"""Run administrative tasks."""
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()
#mark django settings module as settings.py
#os.environ.setdefault("DJANGO_SETTINGS_MODULE",'project.settings')
#instantiate a web sv for django which is a wsgi
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()


#import your models schema
from GraphBot.models import User, Measurement



def DeleteUser(arg_id):
    result = User.objects.filter(id=arg_id)
    result.delete()



def UsersLookup(arg_id):
    result =  User.objects.filter(id=arg_id)
    #print(list(result))
    if not result:
        return False
    return True


def CreateUser(arg_id, name_arg, time_span_arg):
    if len(name_arg) >= 30:
        return False
    user = User(id=arg_id,time_span= time_span_arg, name=name_arg,table_num = 0, selected_num=0)
    user.save()




def MeasurementLookup(arg_id):
    print("in measureetn lookup")
    chopeed = ""
    result = Measurement.objects.filter(id= arg_id, date= datetime.date.today()).values()
    if(len(result) > 0):
        chopeed = result[0]
    if not result:
        print("empty")
        return UserInput.Empty

    elif chopeed['val2'] == None: 
        print("second")
        return UserInput.One 
    else:
        print("third")
        return UserInput.Both

def MeasurementIncertion(arg_id, arg_value1, arg_value2 = None, arg_date = datetime.date.today()):
    arg_average = None
    if(arg_value2 != None):
       arg_average = (arg_value1 + arg_value2 ) / 2
       measure =  Measurement(id= arg_id, val1 =  arg_value1, val2=  arg_value2, average=arg_average, date= arg_date)
       measure.save()
    else : 
       measure = Measurement(id=arg_id, val1= arg_value1, date=arg_date)
       measure.save()

def MeasurementUpdate(arg_id, arg_value2):

    result = Measurement.objects.filter(id= arg_id, date= datetime.date.today())[0]
    average_cal = (result["val1"] + arg_value2 )  / 2 #calculate average
    Measurement.objects.filter(id= arg_id, date= datetime.date.today()).update(val2=arg_value2, average=average_cal)
    print(Measurement.objects.filter(id= arg_id, date= datetime.date.today()).values())



# #Create Operations here
# data_dict={'name':'Nimish','age':23}
# t= Teacher(**data_dict)
# t.save()

# # Read operation logic
# k = list(Teacher.objects.all().filter(age=23))

# print(k)
# #print(f'Hello, I am {t.name}, {t.age} y/o.')