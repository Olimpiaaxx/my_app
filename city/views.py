from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.


def city(request):

    if request.method=='GET':
        #message.info(request, 'Find the popular destinations here')
        return render(request,'city.html')
