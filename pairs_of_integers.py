# Example: Given an array of distinct integer values, count the number of pairs of integers that have difference k. For example, given the array {1, 7, 5, 9, 2, 12, 3} and the difference k = 2, there are four pairs with difference 2: (1, 3), (3, 5), (5, 7), (7, 9).

def countPairsWithDiff(arr, k):
  seen = set()
  count = 0

  for i in arr:
    lower = i - k
    higher = i + k
    
    if lower in seen:
      count += 1
    if higher in seen:
      count += 1

    seen.add(i)

  return count

pairs = [1, 7, 5, 9, 2, 12, 3]
print(countPairsWithDiff(pairs, 2))
