# Example: Given an array of distinct integer values, count the number of pairs of integers that have difference k. For example, given the array {1, 7, 5, 9, 2, 12, 3} and the difference k = 2, there are four pairs with difference 2: (1, 3), (3, 5), (5, 7), (7, 9).

def brute_force(arr, k):
  count = 0
  for i in range(0, len(arr)):
    for j in range(i+1, len(arr)):
      if abs(arr[i] - arr[j]) == k:
        count += 1
  return count

def count_pairs_with_diff_k(arr, k):
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

if __name__ == '__main__':
  pairs = [1, 7, 5, 9, 2, 12, 3]
  print(f'Brute Force: {brute_force(pairs, 2)}, Time: O(N^2), Space: O(N)')
  print(f'Hash table: {count_pairs_with_diff_k(pairs, 2)}, Time: O(N), Space: O(N)')
