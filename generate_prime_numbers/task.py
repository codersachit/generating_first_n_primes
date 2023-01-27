from celery import shared_task
from django.http import HttpResponse
from .models import First_N_Primes
import math

@shared_task
def generate_first_n_primes(n):
    ct = 1
    number = 2
    primes_list = []
    while(ct <= n):
        flag = 0
        max_possible_divisor = int(math.sqrt(number))
        for x in primes_list:
            if(number%x == 0):
                flag = 1
            if(x > max_possible_divisor):
                break
        if(flag == 0):
            primes_list.append(number)
            ct = ct + 1
        number = number + 1
    obj = First_N_Primes.objects.filter(n=n)
    obj.update(status = 'Completed', result = ','.join([str(elem) for elem in primes_list]))


