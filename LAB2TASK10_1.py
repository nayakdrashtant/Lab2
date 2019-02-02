def has_no_e(word):
    check = "e" in str(word)
    if check == True:
        return False
    else:
        return True

x = input("Enter word:")
print("Has No E:",has_no_e(x))
