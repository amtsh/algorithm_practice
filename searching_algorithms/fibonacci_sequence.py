# ------------------------
# Generate Fibonacci sequence of length N
# ------------------------

def fibo(n):
  fibo_arr = [0, 1]

  for i in range(2, n):
    fibo_arr.append(fibo_arr[-1] + fibo_arr[-2])
  return fibo_arr[:n]
