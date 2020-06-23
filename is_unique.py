# Question: Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?

def is_unique_1(str):
  # Description: Use a hash table
  # Time: O(N)
  # Space: O(N)

  hash = {}
  for char in str:
    if char not in hash:
      hash[char] = 1
    else:
      return False
  return True

def is_unique_2(str):
  # Description: Sort string, then iterate thru each pair of adjacent characters to check for duplicates
  # Time: O(N log N)
  # Space: O(1)

  lst = [c for c in str]
  lst.sort()
  for i in range(1, len(lst)):
    if lst[i] == lst[i-1]:
      return False
  return True

if __name__ == '__main__':
  s1 = 'abcde'
  s2 = 'aabce'
  print(is_unique_1(s1), is_unique_2(s1))
  print(is_unique_1(s2), is_unique_2(s2))
