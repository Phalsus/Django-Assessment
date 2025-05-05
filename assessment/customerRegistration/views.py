from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import forms
from . import models

# Create your views here.

def index(request):
    return render(request, 'customerRegistration/index.html')

def feedback(request):
    if request.method == 'POST':
        form = forms.CustomerFeedbackForm(request.POST)
        if form.is_valid():
            feedback = models.customerFeedback()
            feedback.name = form.cleaned_data['name']
            feedback.email = form.cleaned_data['email']
            feedback.feedback = form.cleaned_data['feedback']
            feedback.save()

            return redirect('customerRegistration:viewFeedback')
    else:
        form = forms.CustomerFeedbackForm()
    return render(request, 'customerRegistration/feedback.html', {'form': form})

def viewFeedback(request):
    feedbacks = models.customerFeedback.objects.all()
    return render(request, 'customerRegistration/viewFeedback.html', {'feedbacks': feedbacks})
    