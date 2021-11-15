from django.contrib.auth.models import User
import django_filters
from .models import Event
from django import forms
from django.forms import ModelForm
from django.db import models

class DateInput(forms.DateInput):
    input_type = 'date'

class EventFilter(django_filters.FilterSet):
    class Meta:
        model = Event
        fields = {
            'session_id': ['exact'],
            'category': ['contains'],
            'timestamp': ['range']
        }

    @classmethod
    def filter_for_lookup(cls, f, lookup_type):
        # override date range lookups
        if isinstance(f, models.DateField) and lookup_type == 'range':
            return django_filters.DateRangeFilter, {}

        # use default behavior otherwise
        return super().filter_for_lookup(f, lookup_type)