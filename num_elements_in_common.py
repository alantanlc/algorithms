# Questino: Given two sorted arrays, find the number of elements in common. The arrays are the same length and each has all distinct elements.

def find_num_common_elements(a, b):
  # Time: O(N)
  # Space: O(N)

  map = set()
  for i in a:
    map.add(i)

  count = 0
  for i in b:
    if i in a:
      count += 1

  return count

if __name__ == '__main__':
  a = [13, 27, 35, 40, 49, 55, 59]
  b = [17, 35, 39, 40, 55, 58, 60]
  print(find_num_common_elements(a, b))
