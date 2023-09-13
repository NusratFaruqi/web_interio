from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact

# Create your views here.


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def portfolio(request):
    return render(request, 'portfolio.html')

def blog(request):
    return render(request, 'blog.html')



def contact(request):
    if request.method == "POST":

        contact = Contact()
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        massage = request.POST.get('text')

        contact.name = name
        contact.email = email
        contact.phone = phone
        contact.massage = massage
        contact.save()

        return HttpResponse("<h1> Thanks for contuct us </h1>")

    return render(request, 'contact.html')


def showdata(request):
    contacts = Contact.objects.all()
    data = {'Contact': contacts}
    return render(request, 'showdata.html', data)
