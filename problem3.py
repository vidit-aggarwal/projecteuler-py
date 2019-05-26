import sympy as sp
import math as m
num = 600851475143
i = m.sqrt(num)
while(True):
    if(num%i==0 and sp.isprime(i)):
        print(i)
        break
    else:
        i = sp.prevprime(i)
