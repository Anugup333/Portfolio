from django.shortcuts import render,redirect
from .forms import *
from .models import *
from django.contrib import messages

# Create your views here.
def home_view(request):
    return render(request,'home.html')


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  
            messages.success(request,"Thank You,  Contacting Me! ")  
            return redirect('contact')  
    else:
        form = ContactForm()
    return render(request,'contact.html', {'form': form})



def feedback_view(request):
    feedbacks = Feedback.objects.order_by('-created_at')  # latest first
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Thank You , Submitting the Feedback")
            return redirect('feedback')
    else:
        form = FeedbackForm()
    return render(request, 'feedback.html', {'form': form, 'feedbacks': feedbacks})