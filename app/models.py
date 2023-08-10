from django.db import models
from django.contrib.auth.models import User

application_status = [
    ('new','new'),
    ('on_moderation', 'on_moderation'),
    ('confirmed', 'confirmed'),
    ('cancelled', 'cancelled'),
]
payment_type = [
    ('cash','cash'),
    ('money_transfer', 'money_transfer'),
]
education_type = [
    ('bachelor','bachelor'),
    ('master', 'master'),
]
class Sponsor(models.Model):
    fullname = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=100)
    payment_amount = models.IntegerField()
    legal_entity = models.BooleanField(default=False,null=True)
    organization_name = models.CharField(blank=True,max_length=255)
    spent_money = models.IntegerField(default=0)
    application_status = models.CharField(choices=application_status,max_length=20,default='new')
    payment_type = models.CharField(choices=payment_type,max_length=20,default='money_transfer')
    created_at = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.fullname


class Student(models.Model):
    fullname = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=100)
    university = models.ForeignKey('University',on_delete=models.SET_NULL,null=True)
    education_type = models.CharField(choices=education_type,max_length=20)
    contract_fee = models.IntegerField()
    allocated_money = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True,null=True)


class SponsorByStudent(models.Model):
    student = models.ForeignKey(Student,on_delete=models.SET_NULL,null=True,related_name='sponsors')
    sponsor = models.ForeignKey(Sponsor,on_delete=models.SET_NULL,null=True)
    sponsor_money = models.IntegerField()

class University(models.Model):
    name = models.CharField(max_length=255)
