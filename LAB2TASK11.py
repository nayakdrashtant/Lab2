def avoid_forbidden(word,string):
  count = 0
  word = word.lower()
  string = string.lower()
  for s in string:
    if s in word:
      count += 1
  if count > 0:
    return False
  else:
    return True

word = input("Enter word to check forbidden letters:")
forb = input("Enter forbidden letters string to check:")
print(avoid_forbidden(word,forb))
