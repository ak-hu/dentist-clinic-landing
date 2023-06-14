from django.shortcuts import render
from django.contrib import messages
from .forms import MakeAppointment


def index(request):
    if request.method == 'POST':
        form = MakeAppointment(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.add_message(request, messages.SUCCESS, f"Appointment made successfully!")
            except:
                form.add_error(None, 'Form is NOT saved')

        form = MakeAppointment()

    return render(request, 'clinic/index.html', {'form': form})
