# Example: Design an algorithm to print all permutations of a string. For simplicity, assume all characters are unique.

def permutate(str):
  # Description: A recursive approach. With Base Case and Build, we solve the problem first for a base case (e.g. n = 1) and then try to build up from there. When we get to more complex/interesting cases (often n = 3 or n = 4), we try to build those using the prior solutions.

  # Base case
  if len(str) == 1:
    return str

  # Chop off last character and generate all sub permutations 
  sub_permutations = permutate(str[:-1])

  # For each sub permutation, for each string, insert last character into every location of the string 
  result = []
  for perm in sub_permutations:
    for i in range(len(perm)+1):
      new_string = perm[0:i] + str[-1] + perm[i:]
      result.append(new_string)

  return result

if __name__ == '__main__':
  print(permutate('abc'))
