# Example: Given an array of distinct integer values, count the number of pairs of integers that have difference k. For example, given the array {1, 7, 5, 9, 2, 12, 3} and the difference k = 2, there are four pairs with difference 2: (1, 3), (3, 5), (5, 7), (7, 9).

def brute_force(arr, k):
  count = 0
  for i in range(0, len(arr)):
    for j in range(i+1, len(arr)):
      if abs(arr[i] - arr[j]) == k:
        count += 1
  return count

def binary_search(arr, k):
  start, end = 0, len(arr) - 1
  while start <= end:
    pos = (start + end) // 2
    if k == arr[pos]:
      return True
    elif k < arr[pos]:
      end = pos - 1
    else:
      start = pos + 1

def sort_and_binary_search(arr, k):
  arr.sort()
  count = 0
  for i in range(len(arr)):
    if binary_search(arr[i+1:], arr[i]+k):
      count += 1
  return count 

def hash_table(arr, k):
  seen = set()
  count = 0
  for i in arr:
    if i-k in seen:
      count += 1
    if i+k in seen:
      count += 1
    seen.add(i)
  return count

if __name__ == '__main__':
  pairs = [1, 7, 5, 9, 2, 12, 3]
  print(f'Brute Force: {brute_force(pairs, 2)}, Time: O(N^2), Space: O(N)')
  print(f'Sort and Binary Search: {sort_and_binary_search(pairs, 2)}, Time: O(N log N), Space: O(N)')
  print(f'Hash table: {hash_table(pairs, 2)}, Time: O(N), Space: O(N)')
