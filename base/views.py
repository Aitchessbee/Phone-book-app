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
        return redirect('home')

    return render(request, 'base/contact.html')

def deleteContact(request, pk):
    contact = Contact.objects.get(id=pk)

    if request.method == "POST":
        contact.delete()
        return redirect('home');

    context = {"contact": contact}
    return render(request, 'base/delete.html', context)

def editContact(request, pk):
    contact = Contact.objects.get(id=pk)

    if request.method == "POST":

        contact.name = request.POST.get("name")
        contact.number = request.POST.get("number")

        contact.save()
        

    context = {"contact": contact}
    return render(request, 'base/edit.html', context)