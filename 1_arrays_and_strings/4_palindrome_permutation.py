# Question: Given a string, write a function to check if it is a permutation of a palindrome. A palindrome is a word or phrase that is the same forwards and backwards. A permutation is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.

def is_palindrome_permutation(str):
  # Description: Use a hash table to compute character count of input string. A string that is a permutation of a palindrome contains at most 1 character with odd count.
  # Time: O(N)
  # Space: O(N)

  hash = {}
  for char in str.lower():
    if char == ' ':
      continue 

    if char not in hash:
      hash[char] = 1
    else:
      hash[char] += 1

  num_char_odd = 0
  for key, value in hash.items():
    if value % 2 == 1:
      num_char_odd += 1

  print(hash)

  return num_char_odd <= 1

if __name__ == '__main__':
  s1 = 'Tact Coa'
  print(is_palindrome_permutation(s1))
