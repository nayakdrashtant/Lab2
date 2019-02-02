import math
def mathf(a,x):
   # a = float(a)
    x = float(x)
    for i in range(int(a)):
        a = int(a)
        first = i / 1
        second = (x + a / x) / 2 
        third = math.sqrt(a)
        fourth = third - second
        print(first," ",second," ",third," ",fourth)

a=input("a:")
x=input("x:")
mathf(a,x)
