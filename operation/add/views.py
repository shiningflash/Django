from django.shortcuts import render
from django.http import HttpResponse
from .forms import InputForm

def home(request):
    context = {}
    context['form'] = InputForm()
    return render(request, 'home.html', context)

def addnum(request):
    val1 = int(request.GET["num1"])
    val2 = int(request.GET["num2"])
    sum = val1 + val2
    return render(request, 'result.html', {'result': sum})