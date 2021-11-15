from django.shortcuts import render
from .models import Event
from .serializers import EventSerializer
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics, filters
from rest_framework.filters import SearchFilter, OrderingFilter
import json
import sentry_sdk

def home(request):
    context = {
        'Events': Event.objects.all()
    }
    return render(request, 'events/home.html', context)



@api_view(['POST'])
def add_webapp_data(request):
    serializer = EventSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


class EventAPIView(generics.ListCreateAPIView):
    search_fields = ['=session_id', 'category']
    filter_backends = (SearchFilter, OrderingFilter)
    queryset = Event.objects.all()
    serializer_class = EventSerializer

def click_1(request):
    add.delay(2,2)
    return HttpResponse("""<html><script>window.location.replace('/');</script></html>""")
def click_2(request):
    return HttpResponse("""<html><script>window.location.replace('/');</script></html>""")
def click_3(request):
    return HttpResponse("""<html><script>window.location.replace('/');</script></html>""")