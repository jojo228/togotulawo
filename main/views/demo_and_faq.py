from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse

def faq(request):

    return render(request, template_name = "faq.html")
