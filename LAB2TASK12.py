def uses_all(word,string):
  word = word.lower()
  string = string.lower()
  flag = False
  count = 0
  for st in string:
    if st in word:
      count += 1
  if count == len(string):
    flag = True
  return flag

word = input("Enter word to check:")
string = input("Enter string to check letters in word:")
print(uses_all(word,string))

