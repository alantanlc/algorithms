S = "abppple"
words = ["able", "ale", "apple", "bale", "kangaroo"]

# Process m
m = { word[0]: [] for word in words } 
for word in words:
    m[word[0]].append((word, 0))

# Iterate through each letter in S
found = []
for letter in S:
  if letter not in m:
    pass

  # For each tuple containing this letter
  for t in m[letter].copy():
    if t[1]+1 < len(t[0]):
      new_t = (t[0], t[1]+1)
      next_letter = t[0][t[1]+1] 
      if next_letter not in m:
        m[next_letter] = [new_t]
      else:
        m[next_letter].append(new_t)
      m[letter].remove(t)
    else:
      found.append(t)

longest_word = ''
longest_length = 0
for t in found:
 if t[1] > longest_length:
   longest_length = t[1]
   longest_word = t[0] 

print(m)
print(longest_word)
