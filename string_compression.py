# Question: Implement a method to perform basic string compression using the counts of repeated characters. For example, the string aabcccccaaa would become a2b1c5a3. If the "compressed" string would not become smaller than the original string, your method should return the original string. You can assume the string has only uppercase and lowercase letters (a - z).

def compress(s):
  # Time: O(N)
  # Space: O(N)

  if not s:
    return s

  compressed_string = ''
  count = 1 
  current = s[0] 
  for i, c in enumerate(s[1:]):
    if c != current:
      compressed_string += current + str(count)
      count = 1
      current = c
    else:
      count += 1
  compressed_string += current + str(count)

  return compressed_string if len(compressed_string) < len(s) else s

if __name__ == '__main__':
  s1 = 'aabcccccaaa'
  s2 = 'abcde'
  print(compress(s1))
  print(compress(s2))
