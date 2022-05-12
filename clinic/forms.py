from django import forms
from .models import Appointment


class MakeAppointment(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['name', 'email', 'phone_number', 'date']

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter your full name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter your email'}),
            'phone_number': forms.NumberInput(attrs={'placeholder': 'Enter your number'}),
            'date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }