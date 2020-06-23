# Questino: Given two sorted arrays, find the number of elements in common. The arrays are the same length and each has all distinct elements.

def find_num_common_elements_1(a, b):
  # Description: Throw everything in A into a hash table, this takes up O(N) space. This will take O(N) time. Then, we just go through B and look up each element in the hash table. This look up (or search) os O(1), so our runtime is O(N).
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

def find_num_common_elements_2(a, b):
  # Description: Our best algorithm that doesn't use extra space was the binary search one. Think about BUD. The bottleneck is searching. Is there anything unnecessary or duplicated? It's unnecessary that A[3] = 40 searched over all of B. We know that we just found 35 at B[1], so 40 certainly won't be before 35. Rach binary search should start where the last one left off. In fact, we don't need to do a binary search at all now. We can just do a linear search. As long as the linear search in B is just picking up where the last one left off, we know that we're going to be operating in linear time.
  # Time: O(N)
  # Space: O(1)

  pos = 0
  count = 0
  for i in a:
    while b[pos] <= i: 
      if b[pos] == i:
        count += 1
        break
      pos += 1 
  return count

if __name__ == '__main__':
  a = [13, 27, 35, 40, 49, 55, 59]
  b = [17, 35, 39, 40, 55, 58, 60]
  print(find_num_common_elements_1(a, b))
  print(find_num_common_elements_2(a, b))
