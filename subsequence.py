S = "abppplee"
D = {"able", "ale", "apple", "bale", "kangaroo"}

# Preprocess S
M = {char: [] for char in S}
for i, char in enumerate(S):
  M[char].append(i)

# For each word check for subsequence
for word in sorted(D, key=lambda w: len(w), reverse=True):
  prev_index = -1
  is_subsequence = True
  for char in word:
    if char not in M.keys():
      is_subsequence = False
      break

    # Find smallest index that is larger then prev_index
    next_index = prev_index 
    for i in M[char]:
      if i > prev_index:
        next_index = i
        break
    
    # If next_index is same as prev_index, then subsequence does not exist
    if next_index == prev_index:
      is_subsequence = False
      break
    else: 
      prev_index = next_index

  if is_subsequence:
    print(word)
    break
