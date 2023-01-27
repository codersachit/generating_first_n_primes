from .task import generate_first_n_primes
from .models import First_N_Primes
from django.http import HttpResponse
from .forms import InputFormForN, InputFormForRequestId
from django.shortcuts import render

def input_n_form(request):
    form = InputFormForN()
    return render(request,'generate_prime_numbers/input_n.html',{'form': form})

def input_request_id_form(request):
    form = InputFormForRequestId()
    return render(request,'generate_prime_numbers/input_request_id.html',{'form': form})


def first_n_primes(request):
    form = InputFormForN(request.POST)
    if form.is_valid():
        n = int(form.cleaned_data.get('n'))
        obj = First_N_Primes(n = n, status = 'processing_ongoing', result = '')
        obj.save()
        generate_first_n_primes.delay(n)
        return HttpResponse(f'Status: {obj.status}\nRequest Id: {obj.id}')

def get_first_n_primes(request):
    form = InputFormForRequestId(request.POST)
    if form.is_valid():
        try:
            obj = First_N_Primes.objects.get(id=form.cleaned_data.get('request_id'))
        except First_N_Primes.DoesNotExist:
            return HttpResponse(f'Request id is invalid')
        ans = obj.result
        if(len(ans) == 0):
            return HttpResponse(f'Status: {obj.status}')
        else:
            return HttpResponse(f'Status: {obj.status}\n\n\nResult: {ans}')
    


