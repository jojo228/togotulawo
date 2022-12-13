from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse

def faq(request):

    return render(request, template_name = "faq.html")


def term_condition(request):

    return render(request, template_name = "terms_conditions.html")


def police_privee(request):

    return render(request, template_name = "police_privee.html")
