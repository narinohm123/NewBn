from rest_framework import fields, serializers
from .models import *
from account.models import *
# from account import models 
# from django.contrib.auth.models import User

class Academic_ManpowerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Academic_Manpower
        fields = '__all__'  

class YearSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Year
        fields = '__all__'

class Service_ManpowerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Service_Manpower
        fields = '__all__'

class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

class BudgetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Budget
        fields = '__all__'

class Academice_OutstandSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Academice_Outstand
        fields = '__all__'


class Study_leaveSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Study_leave
        fields = '__all__'

class PendingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pending
        fields = '__all__'
    

class Year_planSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Year_plan
        fields = '__all__'
    
class Human_resourceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Human_resource
        fields = '__all__'

class ReportSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Report
        fields = '__all__'