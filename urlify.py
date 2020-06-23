# Question: Write a method to replace all spaces in a string with '%20'. You may assume that the string has sufficient space at the end to hold the additional characters, and that you are given the "true" length of the string. (Note: If implementing in Java, please use a character array so that you can perform this operation in place.)

def urlify(str, k):
  pos = len(str) - 1
  str = [c for c in str]
  for i in reversed(range(k)):
    if str[i] != ' ':
      str[pos] = str[i]
      pos -= 1
    else:
      str[pos] = '0'
      str[pos-1] = '2'
      str[pos-2] = '%'
      pos -= 3
  return ''.join(str)

if __name__ == '__main__':
  print(urlify('Mr John Smith    ', 13))
