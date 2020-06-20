# Example: Given a smaller string s and a bigger string b, design an algorithm to find all permutations of the shorter string within the longer one. Print the location of each permutation.

def permutation(s1, s2):
  # Description:
  #   Step 1: Compute count of all unique characters in s1 and store in a dict as s1Map
  #   Step 2: Duplicate a copy of s1Map as s2Map
  #   Step 3: Iterate over each character in s2
  #     Case 1: If character exists in s2Map and count of s2Map[character] > 0, decrement s2Map[character] by 1 and increment count by 1. Then if count equals len(s1), a permutation is found, append index to found, decrement count by 1, and increment drop out character count in s2Map by 1. 
  #     Case 2: Else, reset s2Map to s1Map copy and count to 0, and then if this character exists in s2Map, increment s2Map[character] by 1 and decrement count by 1.
  # S = len(s1), B = len(2)
  # Time: O(B)
  # Space: O(S + B)?

  s1Map = {}
  for c in s1:
    if c not in s1Map:
      s1Map[c] = 1
    else:
      s1Map[c] += 1

  s2Map = s1Map.copy()
  count = 0
  found = []
  for pos, c in enumerate(s2):
    print(pos, c, s2Map, count)
    if c in s2Map and s2Map[c] > 0:
      count += 1
      s2Map[c] -= 1
      if count == len(s1):
        print('match!', f'Add back to s2Map: {s2[pos - len(s1) + 1]}')
        found.append(pos - len(s1) + 1)
        count -= 1
        s2Map[s2[pos - len(s1) + 1]] += 1
    else:
      drop = s2[pos - len(s1) + 1]
      if c != drop:
        s2Map = s1Map.copy()
        count = 0
        if c in s2Map:
          s2Map[c] -=1
          count += 1
        
  return found

if __name__ == '__main__':
  print(permutation('abbc', 'cbabadcbbabbcbabaabccbabc'))
