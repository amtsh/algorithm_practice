"""
To calculate a number x raised to power n in (log n) time,

power(x, n) = power(x, n/2) * power(x, n/2)        (if n is even)
power(x, n) = x * power(x, n/2) * power(x, n/2)    (if n is odd)

"""

def power(x, n):
  
  if n is 1:
    return x

  if (n % 2) == 0:
    result = power(x, n//2)
    return result * result
  else:
    result = power(x, n//2)
    return x * result * result

if __name__ == '__main__':
  result = power(2, 16)
  print result