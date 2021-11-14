from .models import Event
from rest_framework import serializers
from django.db import models

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'
    session_id = serializers.CharField(max_length=50)
    category = serializers.CharField(max_length=50)
    name = serializers.CharField(max_length=50)
    data = serializers.JSONField()
    timestamp = serializers.DateTimeField()