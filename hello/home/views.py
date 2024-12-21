from django.shortcuts import render, HttpResponse
from home.models import Contact


def home(request):
    return render(request,'home.html')
def index(request):
    return render(request,'home.html')
def skill(request):
    return render(request,'skill.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    if request.method == 'POST': 
        name = request.POST.get('name')  
        email = request.POST.get('email') 
        msg = request.POST.get('message')  
        contact = Contact(name=name, email=email, msg=msg) 
        contact.save()
    return render(request, 'contact.html')  

