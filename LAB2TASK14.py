def cons(myvar,no):
    myvar = str(myvar)
    no = int(no)
    check = ""
    iscons = False                                                                          
    for w in myvar:                                                                       
        if len(check) == 0:
            check = w                                                                  
        else:
            if len(check) == no:
                iscons = True
            else:
                if w in check:                                                             
                    check = check + w
                else:
                    check = ""
    return iscons

x = input("Enter string:")
y = input("no of consective:")
print("Is ",y, " consecutive:",cons(x,y))