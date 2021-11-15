from django.db import models
from account.models import *

# Create your models here.
class Year(models.Model):
    year = models.CharField(max_length=4)
    def __str__(self):
        return f'{self.year}'


class Academic_Manpower(models.Model):
    year =  models.CharField(max_length=4, null=True)
    faculty = models.CharField(max_length=255, null=True)
    master = models.IntegerField(blank=True,default='-', null=True)
    phd = models.IntegerField(blank=True,default='-', null=True)
    exteach = models.IntegerField(blank=True,default='-', null=True)
    teach = models.IntegerField(blank=True,default='-', null=True)
    asst_prof = models.IntegerField(blank=True,default='-', null=True)
    assoc_prof = models.IntegerField(blank=True,default='-', null=True)
    work = models.IntegerField(blank=True,default='-', null=True)
    leave = models.IntegerField(blank=True,default='-', null=True)
    total = models.IntegerField(null=False)
    def __str__(self):
        return f'{self.faculty}'f' {self.year}'

class Service_Manpower(models.Model):
    year =  models.CharField(max_length=4, null=True)
    s_position = models.CharField(max_length=255, blank=True, null=True)
    s_bhd = models.IntegerField(blank=True,default='-', null=True)
    s_master = models.IntegerField(blank=True,default='-', null=True)
    s_sf = models.IntegerField(blank=True,default='-', null=True)
    s_specific_sf = models.IntegerField(blank=True,default='-', null=True)
    s_prof = models.IntegerField(blank=True,default='-', null=True)
    s_specific_prof = models.IntegerField(blank=True,default='-', null=True)
    s_work = models.IntegerField(blank=True,default='-', null=True)
    s_leave = models.IntegerField(blank=True,default='-', null=True)
    s_total = models.IntegerField(null=False)
    def __str__(self):
        return f'{self.s_position}'f' {self.year}'

class Event(models.Model):
    year =  models.CharField(max_length=4, null=True)
    faculty = models.CharField(max_length=255, null=True)
    total = models.IntegerField(null=False)
    train_people = models.IntegerField(blank=True,default='-', null=True)
    train_time = models.IntegerField(blank=True,default='-', null=True)
    seminar_people = models.IntegerField(blank=True,default='-', null=True)
    seminar_time = models.IntegerField(blank=True,default='-', null=True)
    observe_people = models.IntegerField(blank=True,default='-', null=True)
    observe_time = models.IntegerField(blank=True,default='-', null=True)
    def __str__(self):
        return f'{self.faculty}'f' {self.year}'

class Budget(models.Model):
    faculty = models.CharField(max_length=255, null=True)
    budgetyear = models.CharField(max_length=4)
    initial_budget = models.IntegerField(blank=True,default='-', null=True)
    total_budget = models.IntegerField(blank=True,default='-', null=True)
    balance = models.IntegerField(blank=True,default='-', null=True)
    def __str__(self):
        return f'{self.faculty}'


class Academice_Outstand(models.Model):
    year =  models.CharField(max_length=4, null=True)
    rank = models.CharField(max_length=1)
    type_a = models.CharField(max_length=255, null=True ,default='-')
    name = models.CharField(max_length=255, null=True,default='-')
    type_choice = (
        ('บุคลากรสายวิชาการ','บุคลากรสายวิชาการ'),
        ('บุคลากรสายบริการ','บุคลากรสายบริการ')
    )
    typeps = models.CharField(max_length=50,choices=type_choice)
    def __str__(self):
        return f'{self.year}' f' {self.typeps}'


class Study_leave(models.Model):
    degree_choice = (
        ('ปริญญาโท','ปริญญาโท'),
        ('ปริญญาเอก','ปริญญาเอก')
    )
    degree = models.CharField(max_length=10,choices=degree_choice)
    name = models.CharField(max_length=255)
    university = models.CharField(max_length=255)
    faculty = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    total_time = models.CharField(max_length=255)
    bursary = models.CharField(max_length=255)
    time = models.IntegerField(null=True)
    extend_time = models.IntegerField()
    extend_begin = models.DateField()
    extend_end = models.DateField()
    work = models.DateField()
    approval = models.DateField()
    requesting = models.DateField()
    def __str__(self):
        return f'{self.name}' f'ศึกษาต่อ {self.degree}' f'{self.university}' f' ({self.faculty})'



class Pending(models.Model):
    name = models.CharField(max_length=255)
    date_request = models.DateField()
    date_request_evaluate = models.DateField()
    date_evaluate = models.DateField()
    date_begin = models.DateField()
    date_full_term = models.DateField()
    position_rc = models.CharField(max_length=255)
    situation = models.CharField(max_length=255)
    def __str__(self):
        return f'{self.name}' 

class Year_plan(models.Model):
    year = models.CharField(max_length=9)
    def __str__(self):
        return f'{self.year}'

class Human_resource(models.Model):
    year = models.CharField(max_length=9, null=True)
    file = models.FileField(default='default.pdf',upload_to='uploads/%Y/%m/%d/')
    def __str__(self):
        return f'{self.year}'

class Report(models.Model):
    year = models.CharField(max_length=4, null=True)
    file = models.FileField(default='default.pdf',upload_to='uploads/%Y/%m/%d/')
    def __str__(self):
        return f'{self.year}'