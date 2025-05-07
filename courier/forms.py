from django import forms
from .models import CourierBooking

class CourierBookingForm(forms.ModelForm):
    class Meta:
        model = CourierBooking
        fields = [
            'hub', 'tracking_number', 'sender_name', 'receiver_name',
            'pickup_address', 'delivery_address', 'delivery_date', 'status'
        ]
