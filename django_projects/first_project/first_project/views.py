from django.shortcuts import render
from . import machine_learning_model

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def result(request):
    user_input = request.GET['input1']
    user_input = machine_learning_model.multiplier(user_input)
    inputs = {'home_input': user_input}
    return render(request, 'result.html', inputs)