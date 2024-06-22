from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.http.response import HttpResponse
from saharahco.models import *
import datetime
# Create your views here.

def home(request):
    return render(request,'index.html')

def contact(request):
    context = {}

    if(request.method == "POST"):
        name = request.POST.get("name")
        email = request.POST.get("email")
        message=  request.POST.get('message')
        date = datetime.date.today()

        obj = Contact_us(name = name,email =email,message = message,date = date)
        obj.save()

        context['message'] = f"{name},Thanks for contacting us we will get back to you soon"

    print(name)

    return render(request,'index.html', context)
def service(request):

    ser =  Services.objects.all()
    context = {
        "services": ser
    }
    print(ser)
    return render(request, 'index.html', context)
