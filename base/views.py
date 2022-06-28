from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Contact


# Create your views here.
def home(request):
    contacts = Contact.objects.all()
    context = {"contacts": contacts}

    return render(request, 'base/home.html', context)

def addContact(request):
    if request.method == "POST":
        Contact.objects.create(
            name = request.POST.get("name"),
            number = request.POST.get("number")
        )

    return render(request, 'base/contact.html')