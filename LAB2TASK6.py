def custom_function(string):
    if len(string) <= 3:
        return string
    else:
        check_ing = string[-3:]
        if check_ing == "ing":
            string = string[:-3]
            string = string + "ly"
            return string
        else:
            string = string + "ing"
            return string

string = input("enter custom string:")
print("Output:",custom_function(string))
