from django.shortcuts import render
from .models import Destination

# Create your views here.


def home(request):
    dest1 = Destination()
    dest1.name = 'New York'
    dest1.desc = 'The City That Never Sleeps'
    dest1.img = 'destination_1.jpg'
    dest1.price = 700

    dest2 = Destination()
    dest2.name = 'Sylan'
    dest2.desc = 'Best Boyfriend <3'
    dest2.img = 'destination_2.jpg'
    dest2.price = 650

    dest3 = Destination()
    dest3.name = 'Toronto'
    dest3.desc = 'City of Dreams'
    dest3.img = 'destination_3.jpg'
    dest3.price = 555

    dests = [dest1, dest2, dest3]


    return render(request, 'index.html', {'dests': dests})
