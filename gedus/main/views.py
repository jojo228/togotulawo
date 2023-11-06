from django.shortcuts import render


def coming_soon(request):

    return render(request, "main/comingsoon.html")


def home(request):
    
    return render(request, "main/gedus_index.html")