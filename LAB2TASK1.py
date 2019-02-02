def dsquare_roo(a,x):
    a=float(a)
    x=float(x)
    while True:
        print(x)
        y = (x+a/x)/2
        if abs(y-x) < 0.00001:
            break
        x = y

a = input("a:")
x = input("x:")
dsquare_roo(a,x)

