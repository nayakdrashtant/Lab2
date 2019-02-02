def is_abecedaria(word):
    for i in range(len(word) - 1):
        if word[i] > word[i + 1]:
            return False
    return True


x = input("Word:")
print(is_abecedaria(x))
