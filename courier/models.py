# courier/models.py
from django.db import models
from django.conf import settings

class Hub(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()

    def __str__(self):
        return self.name

class CourierBooking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    hub = models.ForeignKey(Hub, on_delete=models.CASCADE)
    tracking_number = models.CharField(max_length=100, unique=True)
    sender_name = models.CharField(max_length=100)
    receiver_name = models.CharField(max_length=100)
    pickup_address = models.TextField()
    delivery_address = models.TextField()
    booking_date = models.DateTimeField(auto_now_add=True)
    delivery_date = models.DateTimeField(null=True, blank=True)
    status = models.CharField(
        max_length=50,
        choices=[
            ("booked", "Booked"),
            ("in_transit", "In Transit"),
            ("delivered", "Delivered")
        ],
        default="booked"
    )

    def __str__(self):
        return f"{self.tracking_number} - {self.status}"
    

# courier/models.py
# courier/models.py
from django.conf import settings
from django.db import models

class Booking(models.Model):
    tracking_number = models.CharField(max_length=100)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # This is the change
    sender_name = models.CharField(max_length=200)
    receiver_name = models.CharField(max_length=200)
    status = models.CharField(max_length=100, default='Pending')
    booking_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.tracking_number


