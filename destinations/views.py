from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.


def Destinations(request):

    if request.method=='POST':
        message.info(request, 'Find the popular destinations here')
        return render(request,'destinations.html')
