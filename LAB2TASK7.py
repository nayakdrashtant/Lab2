def is_palindrome(string):
    return string == string[::-1]

string = input("Enter string to check palindrome:")
print("Is Palindrome:",is_palindrome(string))
