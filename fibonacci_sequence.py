# ------------------------
# Generate Fibonacci sequence of length N
# ------------------------


def fibonacci_sequence(n):
    sequence = [0, 1]

    for i in range(2, n):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence[:n]


# ------------------------
# Find Fibonacci number at index N
# ------------------------


def fibonacci_at(n):
    if n < 2:
        return n

    a = 0
    b = 1

    for i in range(2, n + 1):
        a, b = b, a + b

    return b
