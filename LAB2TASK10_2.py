def custom_function(words):
    newlist = []
    for i in words:
        check = "e" in str(i)
        if check == False:
            newlist.append(i)
    checklen = len(newlist)
    wordslen = len(words)
    per = 100 * checklen
    per = per / wordslen
    print(newlist)
    print("percentage:",per,"%")

mylist = ["cheer","Dog","Beer","Cat","Dog"]
custom_function(mylist)
