from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    
    SHIFT_CHOICES = (
        ('MORNING_SHIFT', 'Morning_shift'),
        ('DAY_SHIFT', 'Day_shift'),
        ('NIGHT_SHIFT', 'Night_shift'),
    )
    LANG_CHOICES = (
        ('UZBEK', 'Uzbek'),
        ('ENGLISH', 'English'),
        ('RUSSIAN', 'Russian'),
    )
    BLOOD_TYPE_CHOICES = (
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
    )
    GENDER_CHOICES = (
        ('MALE','Male'),
        ('FEMALE','Female'),
    )
    qr_code = models.ImageField(upload_to='users/qr_codes/')
    teacher_rating = models.CharField(max_length=500)
    shift = models.CharField(max_length=200, choices=SHIFT_CHOICES,
                             default=SHIFT_CHOICES[0][0])
    study_lang = models.CharField(max_length=20, choices=LANG_CHOICES,
                                  default=LANG_CHOICES[0][0])
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=500, blank=True, null=True)
    blood_group = models.CharField(max_length=500, choices=BLOOD_TYPE_CHOICES,
                                   blank=True, null=True)
    date_of_birth = models.DateTimeField(blank=True, null=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES,
                              blank=True, null= True)
    pfp = models.ImageField(upload_to='users/images', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)