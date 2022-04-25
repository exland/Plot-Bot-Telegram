from django.test import TestCase
from GraphBot.models import *
import db_handler


# Create your tests here.


class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create(name="tim", id="654", time_span=2, table_num=4, selected_num=0)

    def test_User_name(self):
        obj = User.objects.get(name="tim")
        self.assertEquals(obj.id, 654)
