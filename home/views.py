# home/views.py
from django.shortcuts import render

def home_view(request):
    return render(request, 'home/home.html')

def about_view(request):
    return render(request, 'home/about.html')

def contact_view(request):
    return render(request, 'home/contact.html')

from django.shortcuts import render

def home_view(request):
    carousel_data = [
        {
            'img': 'https://i.pinimg.com/736x/0f/ee/25/0fee25c922f61800938d163c2321999b.jpg',
            'title': 'Swift & Secure Deliveries',
            'desc': 'Trusted by thousands for timely parcel drop-offs.'
        },
        {
            'img': 'https://i.pinimg.com/736x/a7/d4/a4/a7d4a485e166fa7b5047746d7419341d.jpg',
            'title': 'Connected Hubs Nationwide',
            'desc': 'Optimized routes and hub management.'
        },
        {
            'img': 'https://i.pinimg.com/736x/e3/a3/6f/e3a36f0cd78ae2c2a37807ec60e0d30f.jpg',
            'title': 'Live Parcel Tracking',
            'desc': 'Stay updated with real-time tracking.'
        },
    ]

    features = [
        {
            'icon': 'shield-lock-fill',
            'color': 'primary',
            'title': 'Secure Handling',
            'text': 'Every shipment is tracked and packed with utmost care.'
        },
        {
            'icon': 'geo-alt-fill',
            'color': 'success',
            'title': 'Real-Time Location',
            'text': 'Our GPS system keeps you updated on parcel location.'
        },
        {
            'icon': 'headset',
            'color': 'warning',
            'title': '24/7 Support',
            'text': 'We’re here whenever you need help or tracking info.'
        },
    ]

    testimonials = [
        {
            'name': 'Ali Khan',
            'text': 'Reliable and fast service every time. Highly recommended!'
        },
        {
            'name': 'Sara Mehta',
            'text': 'I always use this service for my small business deliveries.'
        },
        {
            'name': 'John D’Souza',
            'text': 'Great support team and accurate tracking!'
        },
    ]

    stats = [
        {'num': '15000', 'label': 'Deliveries'},
        {'num': '1200', 'label': 'Cities Served'},
        {'num': '99.9', 'label': 'Success Rate'},
    ]

    return render(request, 'home/home.html', {
        'carousel_data': carousel_data,
        'features': features,
        'testimonials': testimonials,
        'stats': stats,
    })

