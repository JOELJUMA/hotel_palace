# main/forms.py

from .models import ContactInquiry
from .models import Booking
from django import forms
from .models import Testimonial


class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ['name', 'message', 'image']

# main/forms.py




class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['fullname', 'email', 'phone_number',
                  'room_number', 'check_in_date', 'check_out_date']


# main/forms.py


# main/forms.py


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactInquiry
        fields = ['name', 'email', 'message']


