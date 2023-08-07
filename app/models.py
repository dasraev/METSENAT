from django.db import models
from django.contrib.auth.models import User
from rest_framework.validators import ValidationError

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
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.fullname


class Student(models.Model):
    fullname = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=100)
    university = models.ForeignKey('University',on_delete=models.SET_NULL,null=True)
    education_type = models.CharField(choices=education_type,max_length=20)
    contract_fee = models.IntegerField()
    # sponsors = models.ManyToManyField(Sponsor,related_name='students',null=True)
    allocated_money = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)


class SponsorByStudent(models.Model):
    student = models.ForeignKey(Student,on_delete=models.SET_NULL,null=True,related_name='sponsors')
    sponsor = models.ForeignKey(Sponsor,on_delete=models.SET_NULL,null=True)
    sponsor_money = models.IntegerField()

class University(models.Model):
    name = models.CharField(max_length=255)

#
# class Test(models.Model):
#     name = models.CharField(max_length=2,unique=True,null=True)
#     age = models.IntegerField()
#     asd = models.CharField(blank=True,max_length=255,default='test-default')
#     def full_name(self):
#         return f'{self.name}+www'
#     def __str__(self):
#         return f'{self.name}-{self.asd}'
# class Test2(models.Model):
#     name = models.CharField(max_length=255)
#     age = models.IntegerField()
#     asd = models.CharField(blank=True,max_length=255,default='test-default')
#     def __str__(self):
#         return f'{self.name}-{self.asd}'
#
# class B(models.Model):
#     name2 = models.CharField(max_length=255,blank=True)
#     name3 = models.CharField(max_length=255,blank=True,null=True)
#     name4 = models.CharField(max_length=255,default='')
#     noname = models.CharField(max_length=255,null=True)
#
#     test = models.ForeignKey(Test,on_delete=models.CASCADE,null=True)
#     test2 = models.ManyToManyField(Test2)
#
# class C(models.Model):
#     name2 = models.CharField(max_length=255,blank=True)
#     name3 = models.CharField(max_length=255,blank=True,null=True)
#     name4 = models.CharField(max_length=255,default='')
#     noname = models.CharField(max_length=255)
#
#     test = models.ForeignKey(Test,on_delete=models.CASCADE,null=True)
#     test2 = models.ManyToManyField(Test2)
#
# class shit(models.Model):
#     name = models.CharField(max_length=100,blank=True)
#
#
# from django.db import models
#
class Author(models.Model):
    name = models.CharField(max_length=100)
#
# class Book(models.Model):
#     title = models.CharField(max_length=200)
#     author = models.ForeignKey(Author, on_delete=models.CASCADE)
#     publication_date = models.DateField()
#     test = models.CharField(max_length=255,null=True)
#     # Other fields...
#
#
# # TEST
#
# class School(models.Model):
#     name = models.CharField(max_length=100,null=True)
#
# class Pupil(models.Model):
#     name = models.CharField(max_length=100,null=True)
#     school = models.ForeignKey(School,on_delete=models.SET_NULL,null=True)
