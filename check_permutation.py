# Question: Given two strings, write a method to decide if one is a permutation of the other.

def check_permutation(s1, s2):
  # Description: Throw characters in s1 into a character frequency hash table. Subtract character frequency in hash table for each character in s2.
  # Time: O(N)
  # Space: O(N)

  s1Map = {}
  for c in s1:
    if c not in s1Map:
      s1Map[c] = 1
    else:
      s1Map[c] += 1

  for c in s2:
    if c not in s1Map:
      return False
    else:
      if s1Map[c] == 0:
        return False
      else:
        s1Map[c] -= 1

  return True

if __name__ == '__main__':
  s1 = 'abcd'
  s2 = 'bcda'
  s3 = 'abce'
  print(check_permutation(s1, s2))
  print(check_permutation(s1, s3))
