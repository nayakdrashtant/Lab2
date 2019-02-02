def read_file(file):
    f = open(file,"r")
    for i in f:
        i = i.strip()
        if len(i) > 20:
            print(i)

file = input("Enter name of file:")
read_file(file)
