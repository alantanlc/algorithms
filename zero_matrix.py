# Question: Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column are set to 0.

def zero_matrix(matrix):
  # Time: O(MxN)
  # Space: O(1)
  
  for m in range(len(matrix)):
    for n in range(len(matrix[m])):
      if matrix[m][n] == 0:
        matrix[m][0] = 0
        matrix[0][n] = 0

  for m in range(len(matrix)):
    for n in range(len(matrix[m])):
      if matrix[m][0] == 0 or matrix[0][n] == 0:
        matrix[m][n] = 0

  return matrix

if __name__ == '__main__':
  matrix = [[1,2,3],[4,0,6],[7,8,9]]
  print(zero_matrix(matrix))
