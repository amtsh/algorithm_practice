# ------------------------
# Given a sorted list, find the position of an item in the list using binary search.
# ------------------------
def bin_search(x, L):
  low = 0
  high = len(L) - 1

  while low <= high:
    midpoint_index = int((low + high)/2)
    midpoint_value = L[midpoint_index]

    if x == midpoint_value:
      return midpoint_index
    if x < midpoint_value:
      high = midpoint_index - 1
    else:
      low = midpoint_index + 1

  return -1
