from .models import CarouselImage, CarouselItem, Testimonial, Room, Blog, Booking, AboutUs
from django.shortcuts import render
import requests
from .forms import BookingForm
from django.http import HttpResponse
from django.views import View
from django.shortcuts import render, redirect
from .models import CarouselImage, Testimonial, Room, Blog, Contact, CarouselItem, Booking


# main/views.py

from django.core.mail import send_mail
from .models import ContactInquiry
from .forms import ContactForm
from django.conf import settings


# main/views.py
# main/views.py




def index(request):
    # ... (existing code)

    blogs = Blog.objects.all()

    return render(request, 'main/index.html', {
        # ... (existing context)
        'blogs': blogs,
    })







# main/views.py


from .models import AboutUs


def about_us(request):
    # Assuming you have only one AboutUs entry
    about_us_data = AboutUs.objects.first()
    return render(request, 'main/about_us.html', {'about_us_data': about_us_data})



def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            inquiry = form.save()

            # Send email to joeljuma0020@gmail.com with the inquiry details
            send_mail(
                'New Contact Inquiry',
                f'Name: {inquiry.name}\nEmail: {
                    inquiry.email}\nMessage: {inquiry.message}',
                'joeljuma0020@gmail.com',  # Change to your email
                ['joeljuma0020@gmail.com'],
                fail_silently=False,
            )

            # Redirect to clear the form after submission
            return redirect('contact_us')
    else:
        form = ContactForm()

    return render(request, 'main/contact_us.html', {'form': form})




# main/views.py


def index(request):
    carousel_images = CarouselImage.objects.all()
    carousel_items = CarouselItem.objects.all()
    testimonials = Testimonial.objects.all()
    rooms = Room.objects.all()
    blogs = Blog.objects.all()
    bookings = Booking.objects.all()

    # Assuming you have only one AboutUs entry
    about_us_data = AboutUs.objects.first()

    return render(request, 'main/index.html', {
        'carousel_images': carousel_images,
        'carousel_items': carousel_items,
        'testimonials': testimonials,
        'rooms': rooms,
        'blogs': blogs,
        'bookings': bookings,
        'about_us_data': about_us_data,  # Pass the AboutUs data to the template
    })


# main/views.py


class BookingView(View):
    template_name = 'main/booking.html'

    def get(self, request, *args, **kwargs):
        form = BookingForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save()

            # Replace these placeholders with your actual M-Pesa Daraja credentials
            consumer_key = 'BpUeW0NAfxTQ3dNbq1BF2npqpopmaJRZ'
            consumer_secret = 'iTw0ZA0Iguj3igiE'
            phone_number = 799304451
            passkey = 'bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919'

            # Call M-Pesa Daraja API to initiate payment
            payment_url = 'https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest'

            headers = {
                'Authorization': 'bjyAcAwYuX3kw670r7gGHQGJTHm4',  # Replace YOUR_ACCESS_TOKEN
                'Content-Type': 'application/json',
            }

            payload = {
                'BusinessShortCode': '174379',
                'Password': 'MTc0Mzc5YmZiMjc5ZjlhYTliZGJjZjE1OGU5N2RkNzFhNDY3Y2QyZTBjODkzMDU5YjEwZjc4ZTZiNzJhZGExZWQyYzkxOTIwMTYwMjE2MTY1NjI3',  # Generate the password using Lipa Na M-Pesa Online API
                'Timestamp': '20160216165627',  # Replace with current timestamp
                'TransactionType': 'CustomerPayBillOnline',
                'Amount': 1,  # Replace with the actual amount
                'PartyA': 254799304451,
                'PartyB': '174379',
                'PhoneNumber': 254799304451,
                'CallBackURL': 'YOUR_CALLBACK_URL',
                'AccountReference': 'CompanyXLTD',
                'TransactionDesc': 'Payment for room booking',
            }

            response = requests.post(
                payment_url, json=payload, headers=headers)

            if response.status_code == 200:
                # Payment initiated successfully, you may redirect the user to the payment confirmation page
                return redirect('payment_confirmation')
            else:
                # Handle the error appropriately
                return HttpResponse("Failed to initiate payment")

        return render(request, self.template_name, {'form': form})
