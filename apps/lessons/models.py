from django.db import models
from django.contrib.auth.models import User
from apps.common.models import BaseModel



class Subject(BaseModel):
    name = models.CharField(max_length=200)



class Teacher(BaseModel):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone_number = models.CharField(max_length=20)
    pfp = models.ImageField(upload_to='students/pfps')
    subject = models.ManyToManyField(Subject)

class Class(BaseModel):
    name = models.CharField(max_length=200)
    capacity = models.PositiveSmallIntegerField(default=30)
    major = models.CharField(max_length=200, null=True, blank=True)
    curator = models.ForeignKey(Teacher, models.PROTECT)
    room_number = models.CharField(max_length=200)


class Student(BaseModel):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone_number = models.CharField(max_length=20)
    pfp = models.ImageField(upload_to='students/pfps')