def quicksort(A):
  if len(A) == 1 or len(A) == 0:
    return A

  pivot = len(A) - 1

  lesser = [x for x in A[:-1] if x < A[pivot]]
  greater = [x for x in A[:-1] if x > A[pivot]]

  return quicksort(lesser) + [A[pivot]] + quicksort(greater)

print(quicksort([2,1,3, 12,0,234,222]))
