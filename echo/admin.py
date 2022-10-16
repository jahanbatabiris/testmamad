from django.contrib import admin
from .models import Room


# Register your models here.

class RoomAdmin(admin.ModelAdmin):

    list_display = ("connected_user","room_group_name","is_started")

admin.site.register(Room,RoomAdmin)
