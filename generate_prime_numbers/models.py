from django.db import models

class First_N_Primes(models.Model):
    n = models.IntegerField()
    result = models.TextField(blank=True)
    status = models.CharField(max_length=30)

    def __str__(self):
        return f'Result of {self.n}'

    



