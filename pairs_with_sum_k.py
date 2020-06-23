# Example: Find all pairs with sum k within an array (assuming all distinct elements).

def find_pairs_with_sum_k(arr, k):
  # Time: O(N)
  # Space: O(N)

  if not arr:
    return

  pairs = []
  map = {arr[0]} 

  for i in arr[1:]:
    if k-i in map:
      pairs.append((i, k-i))
    map.add(i)
  return pairs

if __name__ == '__main__':
  arr = [1,3,5,0,2,4]
  k = 5
  print(find_pairs_with_sum_k(arr, k))
