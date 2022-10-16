from django.db import models

# Create your models here.
from pyasn1.compat.octets import null


class Room(models.Model):
    code = models.CharField(max_length=255, blank=True)
    connected_user = models.IntegerField(default=1)
    room_group_name = models.CharField(max_length=255, blank=True, null=True)
    is_started = models.BooleanField(default=False)