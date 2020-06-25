# Question: Assume you have a method is_substring which checks if one word is a substring of another. Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only one call to is_substring (e.g. 'waterbottle' is a rotation of 'erbottlewat').

def is_substring(s1, s2):
  return s2 in s1

def is_rotation(s1, s2):
  # Time: The runtime of this varies based on the runtime of is_substring. But if you assume that is_substring runs in O(A+B) time (on strings of length A and B), then the runtime of is_rotation is O(N). 
  # Space: O(A)

  # Check that s1 and s2 are equal length and not empty
  if len(s1) == len(s2) and s1:
    s3 = s1 + s1
    return is_substring(s3, s2)
  return False

if __name__ == '__main__':
  s1 = 'waterbottle'
  s2 = 'erbottlewat'
  print(is_rotation(s1, s2))
