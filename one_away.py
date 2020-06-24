# Question: There are three types of edits that can be performed on strings: insert a character, remove a character, or replace a character. Given two strings, write a function to check if they are one edit (or zero edits) away.

def one_edit_away(first, second):
  # Time: O(N)
  # Space: O(1)

  if len(first) == len(second):
    return one_edit_replace(first, second)
  elif (len(first) + 1) == len(second):
    return one_edit_insert(first, second)
  elif (len(first) - 1) == len(second):
    return one_edit_insert(second, first)
  return False

def one_edit_replace(s1, s2):
  found_difference = False
  for i in range(len(s1)):
    if found_difference:
      return False
    found_difference = True
  return True

def one_edit_insert(s1, s2):
  index_1 = 0
  index_2 = 0
  while index_2 < len(s2) and index_1 < len(s1):
    if s1[index_1] != s2[index_2]:
      if index_1 != index_2:
        return False
      index_2 += 1
    else:
      index_1 += 1
      index_2 += 1
  return True

if __name__ == '__main__':
  s1 = 'pale'
  s2 = 'ple'
  s3 = 'bake'
  print(one_edit_away(s1, s2))
  print(one_edit_away(s1, s3))
