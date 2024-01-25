from django.shortcuts import render, redirect
# from .models import Fizzbuzz
from .forms import FizzbuzzForm
# Create your views here.

def logic(number):
        
        if number % 3 == 0 and number % 5 == 0:
            return 'FizzBuzz'
        elif number % 3 == 0:
            return 'Fizz'
        elif number % 5 == 0:
            return 'buzz'
        else:
            return number

def fizzbuzz_view(request):
    form = FizzbuzzForm(request.POST or None)
    result = None
    
    if form.is_valid():
        number = form.cleaned_data.get('number')
        result = logic(number)

    return render(request, 'logic/index.html', {'form': form, 'result': result})