# courier/views.py




from django.shortcuts import render, redirect, get_object_or_404
from .models import CourierBooking
from .forms import CourierBookingForm
from django.contrib.auth.decorators import login_required

@login_required
def booking_list(request):
    bookings = CourierBooking.objects.filter(user=request.user)
    return render(request, 'courier/booking_list.html', {'bookings': bookings})

@login_required
def booking_create(request):
    if request.method == 'POST':
        form = CourierBookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            return redirect('courier:booking_list')  # ✅ Correct namespaced name
    else:
        form = CourierBookingForm()
    return render(request, 'courier/booking_form.html', {'form': form, 'title': 'Create Booking'})

@login_required
def booking_update(request, pk):
    booking = get_object_or_404(CourierBooking, pk=pk, user=request.user)
    if request.method == 'POST':
        form = CourierBookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('courier:booking_list')  # ✅ Correct namespaced name

    else:
        form = CourierBookingForm(instance=booking)
    return render(request, 'courier/booking_form.html', {'form': form, 'title': 'Update Booking'})

@login_required
def booking_delete(request, pk):
    booking = get_object_or_404(CourierBooking, pk=pk, user=request.user)
    if request.method == 'POST':
        booking.delete()
        return redirect('courier:booking_list')  # ✅ Correct namespaced name

    return render(request, 'courier/booking_confirm_delete.html', {'booking': booking})

