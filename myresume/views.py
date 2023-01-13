from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail

# Create your views here.

def home(request):
     return render(request, 'home.html', {})

def about(request):
     return render(request, 'about.html', {})


def resume(request):
     return render(request, 'resume.html', {})


def contact(request):
   if request.method == "POST":
      message_name = request.POST['message-name']
      message_email = request.POST['message-email']
      mes_message = request.POST['message']

      #send an email
      send_mail(
         message_name, # subject
         mes_message, #message
         message_email, #from Email
         ['codewithben1@gmail.com'], #To Email

       )
      


      return render(request, 'contact.html', {'message_name': message_name})
   else:
     return render(request, 'contact.html', {})

