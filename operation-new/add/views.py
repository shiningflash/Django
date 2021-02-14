from django.shortcuts import render
from django.http import HttpResponse

def home(request):    
    
    val1 = request.POST.get('num1')
    val2 = request.POST.get('num2')
    
    sum = None
    
    if val1 and val2:
        sum = int(val1) + int(val2)
        
    context = {
        'val1': val1,
        'val2': val2,
        'result': sum
    }
    
    return render(request, 'home.html', context)
