from django.db.models import query
from django.db.models.fields import EmailField
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import response, viewsets

from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *

from .models import *
from rest_framework.exceptions import AuthenticationFailed

# Create your views here.

# @api_view(['GET'])
# def Academic_power(request):

#     data = Academic_Manpower.objects.all()
#     serializer = Academic_ManpowerSerializer(data,many=True)
#     return Response(serializer.data)

class Year(viewsets.ModelViewSet):
    queryset = Year.objects.all()
    serializer_class = YearSerializer

class Academic_power(viewsets.ModelViewSet):
    queryset = Academic_Manpower.objects.all()
    serializer_class = Academic_ManpowerSerializer

class Service_Manpower(viewsets.ModelViewSet):
    queryset = Service_Manpower.objects.all()
    serializer_class = Service_ManpowerSerializer

class Event(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class Budget(viewsets.ModelViewSet):
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer

class Academice_Outstand(viewsets.ModelViewSet):
    queryset = Academice_Outstand.objects.all()
    serializer_class = Academice_OutstandSerializer

class Study_leave(viewsets.ModelViewSet):
    queryset = Study_leave.objects.all()
    serializer_class = Study_leaveSerializer

class Pending(viewsets.ModelViewSet):
    queryset = Pending.objects.all()
    serializer_class = PendingSerializer


class Year_plan(viewsets.ModelViewSet):
    queryset = Year_plan.objects.all()
    serializer_class = Year_planSerializer

class Human_resource(viewsets.ModelViewSet):
    queryset = Human_resource.objects.all()
    serializer_class = Human_resourceSerializer

class Report(viewsets.ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer