# Example: Given a smaller string s and a bigger string b, design an algorithm to find all permutations of the shorter string within the longer one. Print the location of each permutation.

def permutation(s1, s2):
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
        print('match!', f'pos: {pos}', len(s1), pos - len(s1) + 1, f'to add back: {s2[pos - len(s1) + 1]}')
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
