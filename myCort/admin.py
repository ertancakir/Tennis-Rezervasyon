from django.contrib import admin

# Register your models here.

from .models import Reservation, Users

admin.site.register(Reservation)
admin.site.register(Users)
