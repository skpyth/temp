from django.db import models

# Create your models here.

class Student(models.Model):
    SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    dob = models.DateTimeField(verbose_name="dob",)
    shirt = models.CharField(max_length=50,choices=SHIRT_SIZES)
    email = models.EmailField()
    file = models.FileField()
    photo = models.ImageField()


