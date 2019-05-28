a = 999
b = 999
c = 999
answer = 0
while(True):
    pal = a * b
    print(a, b, pal)
    pal = str(pal)
    if pal == pal[::-1]:
        if answer < int(pal):
            answer = int(pal)
        b -= 1
    elif b <= 100 and a > 100:
        a -= 1
        c -= 1
        b = c
    elif b > 100 and a > 100:
        b -= 1
    else:
        break
print(answer)
