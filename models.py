from django.core.validators import RegexValidator
from django.db import models


class Appointment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+48999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=12, blank=True)
    date = models.DateTimeField(auto_now_add=False, auto_now=False)
