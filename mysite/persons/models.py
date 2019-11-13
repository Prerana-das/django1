from django.db import models
from django.db.models import IntegerField, CharField, BooleanField

genders = [
    ('MALE', 'male'),
    ('FEMALE', 'female'),
    ('OTHERS', 'others')
]


class Person(models.Model):
    id = IntegerField(null=False, primary_key=True)
    name = CharField(max_length=100, null=False)
    age = IntegerField(null=False)
    gender = CharField(choices=genders, null=False, max_length=10)
    bio = CharField(null=False, max_length=500)
    address =CharField(null=False, max_length=50,default="")

    def __str__(self):
        return "{id} {name}".format(id=self.id, name=self.name)