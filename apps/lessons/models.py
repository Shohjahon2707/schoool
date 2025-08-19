from django.db import models
from django.contrib.auth.models import User
from apps.common.models import BaseModel
from django.urls import reverse



class Subject(BaseModel):
    name = models.CharField(max_length=200)
    def get_absolute_url(self):
        return reverse('class_detail', kwargs={'pk': self.pk})
    def __str__(self):
        return self.name
class Teacher(BaseModel):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone_number = models.CharField(max_length=20)
    pfp = models.ImageField(upload_to='students/pfps')
    subject = models.ManyToManyField(Subject)
    def get_absolute_url(self):
        return reverse('teacher_detail', kwargs={'pk': self.pk})


    def __str__(self):
        return f"{self.first_name} {self.last_name}"
class Class(BaseModel):
    name = models.CharField(max_length=200)
    capacity = models.PositiveSmallIntegerField(default=30)
    major = models.CharField(max_length=200, null=True, blank=True)
    curator = models.ForeignKey(Teacher, models.PROTECT)
    room_number = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name} (Room {self.room_number})"
    def get_absolute_url(self):
        return reverse('class_detail', kwargs={'pk': self.pk})

class Student(BaseModel):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone_number = models.CharField(max_length=20)
    pfp = models.ImageField(upload_to='students/pfps')
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    def get_absolute_url(self):
        return reverse('student_detail', kwargs={'pk': self.pk})