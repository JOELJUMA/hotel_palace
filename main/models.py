from django.db import models


class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    message = models.TextField()
    image = models.ImageField(upload_to='testimonials/')

    def __str__(self):
        return self.name


class CarouselItem(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='carousel_images/')
    caption = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class CarouselImage(models.Model):
    image = models.ImageField(upload_to='carousel_images/')
    title = models.CharField(max_length=255)


class Room(models.Model):
    image = models.ImageField(upload_to='rooms/')
    features = models.TextField()


class Blog(models.Model):
    image = models.ImageField(upload_to='blogs/')
    title = models.CharField(max_length=255)
    content = models.TextField()


class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()

# main/models.py
# main/models.py
# main/models.py


class ContactInquiry(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.email}"

# main/models.py

# main/models.py


class Blog(models.Model):
    image = models.ImageField(upload_to='blogs/')
    title = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return self.title


class AboutUs(models.Model):
    mission = models.TextField()
    vision = models.TextField()
    goal = models.TextField()
    mission_statement = models.TextField()

    def __str__(self):
        return "About Us"


class Room(models.Model):
    image = models.ImageField(upload_to='rooms/')
    features = models.TextField()
    # Add any additional fields as needed

    def __str__(self):
        return f"Room {self.id}"


# main/models.py



class Booking(models.Model):
    fullname = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    room_number = models.IntegerField()
    check_in_date = models.DateField()
    check_out_date = models.DateField()

    def __str__(self):
        return f"{self.fullname} - Room {self.room_number}"
