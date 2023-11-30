
from .models import AboutUs
from .models import ContactInquiry
from .models import CarouselImage, Testimonial, Room, Blog, Contact, CarouselItem, Booking
from django.contrib import admin

admin.site.register(CarouselImage)
admin.site.register(Room)
admin.site.register(Blog)
admin.site.register(Contact)
@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    # Ensure that TestimonialForm is correctly imported
    # from .forms import TestimonialForm
    list_display = ('name', 'message',)


@admin.register(CarouselItem)
class CarouselItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'caption',)

# main/admin.py

# main/admin.py
# main/admin.py


admin.site.register(ContactInquiry)
# main/admin.py


@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ('id', 'mission', 'vision', 'goal', 'mission_statement')








@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'email', 'phone_number',
                    'room_number', 'check_in_date', 'check_out_date')

