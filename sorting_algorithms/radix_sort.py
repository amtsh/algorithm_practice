def radix_sort(A):
  passes = len(str(max(A)))
  A = do_padding(A, passes)

  bucket = [[],[],[],[],[],[],[],[],[],[]]

  for i in range(1,passes+1):
    for x in A:
      digit = int(x[i*-1])
      bucket[digit].append(x)

    A = []
    for b in bucket:
      A = A + b
    bucket = [[],[],[],[],[],[],[],[],[],[]]

  return [int(x) for x in A]


def do_padding(A, passes):
  for i in range(len(A)):
    num_str = str(A[i])
    A[i] = ('0' * (passes - len(num_str))) + num_str
  return A

if __name__ == '__main__':
  print radix_sort([23,45,67,54,100, 1000, 0, 34])