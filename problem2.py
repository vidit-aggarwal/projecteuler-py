def fibonacci(n):
    if(n==0):
        return 0
    elif(n==1):
        return 1
    else:
        return (fibonacci(n-1)+fibonacci(n-2))
sum = 0
i = 0
c = 0
while(c <= 4000000):
    c = fibonacci(i)
    if(c%2 == 0):
        sum += c
    i+=1
print(sum)