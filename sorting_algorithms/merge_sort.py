"""
Merge sort is a divide-and-conquer algorithm based on the idea of 
breaking down a list into several sub-lists until each sublist consists of a single element
and merging those sublists in a manner that results into a sorted list.

Time complexity: O(nlogn) for all best, average, worst cases
Space complexity: O(n) as we use temporary array to merge
"""

def merge_sort(A):
  
  length = len(A)
  
  if length == 1:
    return A

  midpoint = length // 2
  A_left = A[:midpoint]
  A_right = A[midpoint:]

  A_left_sorted = merge_sort(A_left)
  A_right_sorted = merge_sort(A_right)

  return merge(A_left_sorted, A_right_sorted)

def merge(A, B):
  result = []

  i = j = 0

  while i < len(A) and j < len(B):
    if A[i] < B[j]:
      result.append(A[i])
      i += 1
    else:
      result.append(B[j])
      j += 1

  while i < len(A):
    result.append(A[i])
    i+=1

  while j < len(B):
    result.append(B[j])
    j+=1

  return result

if __name__ == '__main__':
  result = merge_sort([12, 9, 2, 4, 16, 3])
  print result