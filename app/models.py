import uuid
from django.db import models
import json

class Event(models.Model):
    session_id = models.CharField(db_index=True, max_length=50)
    category = models.CharField(db_index=True, max_length=50)
    name = models.CharField(max_length=50)
    data = models.JSONField()
    timestamp = models.DateTimeField(db_index=True)