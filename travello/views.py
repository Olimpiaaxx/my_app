from django.shortcuts import render
from .models import Destination

# Create your views here.


def home(request):
    dest1 = Destination()
    dest1.name = 'London'
    dest1.desc = 'The City That Never Sleeps'
    dest1.img = 'destination_1.jpg'
    dest1.price = 700
    dest1.offer = False

    dest2 = Destination()
    dest2.name = 'Paris'
    dest2.desc = 'The City of Love'
    dest2.img = 'destination_2.jpg'
    dest2.price = 650
    dest2.offer = False

    dest3 = Destination()
    dest3.name = 'Warsaw'
    dest3.desc = 'The City of Culture'
    dest3.img = 'destination_3.jpg'
    dest3.price = 555
    dest3.offer = False

    dests = [dest1, dest2, dest3]


    return render(request, 'index.html', {'dests': dests})
