import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DRF_Pagination.settings')
import django
django.setup()

from testapp.models import Student
from faker import Faker
from random import randrange
import time
fake = Faker()

def create_students(num_students):
    for i in range(num_students):
        # time.sleep(1000)
        fakeName =  fake.name()
        fakeRoll = randrange(1,120)
        fakeAddress = fake.city()
        print(fakeName)
        print(fakeRoll)
        print(fakeAddress)
        time.sleep(0.01)
        Student.objects.create(name=fakeName,roll=fakeRoll,address=fakeAddress)
        # Student.objects.create(ename=fakeName,esal=fakeRoll,eaddress=fakeAddress)
create_students(120)