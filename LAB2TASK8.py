def rotate_word(word,num):
  newstring = ""
  for ind in word:
    s = ord(ind)
    s = int(s) + int(num)
    s = str(chr(s))
    newstring += s

  print(newstring)

string = input("Enter string for rotate operation:")
num = input("Enter number to rotate string:")
rotate_word(string,num)
