# courier/admin.py
from django.contrib import admin
from .models import CourierBooking, Hub

admin.site.register(CourierBooking)
admin.site.register(Hub)
