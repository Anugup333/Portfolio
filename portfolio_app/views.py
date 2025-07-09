from django.shortcuts import render,redirect
from .forms import *

# Create your views here.
def home_view(request):
    return render(request,'home.html')

def about_view(request):
    return render(request,'about.html')

def contact_view(request):
    success = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  
            success = True
            form = ContactForm()
    else:
        form = ContactForm()
    return render(request,'contact.html', {'form': form,'success':success})
