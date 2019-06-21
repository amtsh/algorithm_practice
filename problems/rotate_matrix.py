"""
You are given an n x n 2D matrix representing an image.
Rotate the image by 90 degrees (clockwise).

Solution: Tranpose the matrix and interchange columns will give the resulting matrix.
"""

def transpose(matrix):
  rows = len(matrix)
  columns = len(matrix[0])

  for row in range(rows):
    for col in range(columns):
      if row < col:
        matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]

  return matrix


def swap_columns(matrix):
  rows = len(matrix)
  columns = len(matrix[0])

  start = 0
  end = columns - 1

  while start < columns //2:

    for row in range(rows):
      matrix[row][start], matrix[row][end] = matrix[row][end], matrix[row][start]

    start += 1
    end -= 1

  return matrix

def print_m(matrix):
  rows = len(matrix)
  columns = len(matrix[0])

  for row in range(rows):
    print("")
    for col in range(columns):
      print(matrix[row][col], end='')
  print("")


matrix = [[1,2,3], [4,5,6], [7,8,9]]

transpose_matrix = transpose(matrix)
result = swap_columns(transpose_matrix)

print_m(result)