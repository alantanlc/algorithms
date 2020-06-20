# Example: Print all positive integer solutions to the equation a^3 + b^3 = c^3 + d^3 where a, b, c, and d are integers between 1 and 1000.

def brute_force_1():
  # Description: A brute force solution with four nested for loops. This algorithm iterates through all possible values of a, b, c, and d and checks if that combination happens to work.
  # Time: O(N^4)
  # Space: O(1)
  n = 1000
  for a in range(1, n):
    for b in range(1, n):
      for c in range(1, n):
        for d in range(1, n):
          if a**3 + b**3 == c**3 + d**3:
            print(a, b, c, d)

def brute_force_2():
  # Description: It's unnecessary to continue checking for other possible values of d. Only one could work. We should at least break after we find a valid solution.
  # Time: O(N^4)
  # Space: O(1)
  n = 1000
  for a in range(1, n):
    for b in range(1, n):
      for c in range(1, n):
        for d in range(1, n):
          if a**3 + b**3 == c**3 + d**3:
            print(a, b, c, d)
            break

def brute_force_3():
  # Description: Is there anything else that is unnecessary? Yes. If there's only one valid d value for each (a, b, c), then we can just compute it. This is just simple math: d = (a**3 + b**3 - c**3) ** (1/3). The 'if' statement is important. We will always find a value for d, but we need to check that it's the right integer value.
  # Time: O(N^3)
  # Space: O(1)
  n = 1000
  for a in range(1, n):
    for b in range(1, n):
      for c in range(1, n):
        d = a**3 + b**3 - c**3
        if d > 0:
          d = int(d**(1.0/3.0))
          if a**3 + b**3 == c**3 + d**3:
            print(a, b, c, d)

def hash_table_1():
  # Description: The brute force algorithms operates by essentially iterating through all (a, b) pairs and then searching all (c, b) pairs to find if there are any matches to that (a, b) pair. Why do we keep on computing all (c, d) pairs for each (a, b) pair? We should just create the list of (c, d) pairs once. Then, we have an (a, b) pair, find the matches within the (c, d) list. We can quickly locate the matches by inserting each (c, d) pair into a hash table that maps from the sum to the pair (or, rather, the list of pairs that have the sum).
  # Time: O(N^2)
  # Space: O(N^2)?
  n = 1000
  map = {}
  for c in range(1, n):
    for d in range(1, n):
      result = c**3 + d**3
      if result not in map:
        map[result] = [(c, d)]
      else:
        map[result].append((c, d))
  for a in range(1, n):
    for b in range(1, n):
      result = a**3 + b**3
      pairs = map[result]
      for pair in pairs:
        print(a, b, pair) 

if __name__ == '__main__':
  # print(brute_force_1())
  # print(brute_force_2())
  # print(brute_force_3())
  print(hash_table_1())
