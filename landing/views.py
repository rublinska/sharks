from django.shortcuts import render
from .forms import UserForm
from event.models import Event
from event.models import EventImage
from datetime import date


# Create your views here.
def landing(request):
    form = UserForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        print(form.cleaned_data)

    events = Event.objects.all()
    event_images = EventImage.objects.all()
    return render(request, 'landing/landing.html', locals())

