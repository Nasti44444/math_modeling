a=1
b=1
for _ in range (0, 1000000, 1):
    c=a+b
    a=b
    b=c
    print(c)