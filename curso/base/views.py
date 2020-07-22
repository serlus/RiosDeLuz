from django.core.mail import send_mail
from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'base/home.html')


# send an mail 

send_mail(
    , # subject
    , # message
    , # from email
    , # to email
)
