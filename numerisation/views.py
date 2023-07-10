from django.conf import settings
from django.shortcuts import render
from numerisation.forms import ContactForm
from django.core.mail import send_mail


# Create your views here.
def home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            # Send email
            send_mail(
                'Formulaire de contact',
                f'Nom: {name}\nEmail: {email}\nMessage: {message}',
                email,  # Replace with your email address
                [settings.EMAIL_HOST_USER],  # Replace with recipient email address(es)
                fail_silently=False,
            )
            return render(request, 'success.html')  # Create success.html template
    else:
        form = ContactForm()
    
    return render(request, "numerisation.html", {'form': form})

