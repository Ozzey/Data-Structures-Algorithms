# Given a number n, find the fibonacci number corresponding to the number

# 1 1 2 3 5 8....

# Recursive Solution
def fibonacci_rec(n):
    if n == 0:
        return 1
    if n == 1:
        return 1

    return fibonacci_rec(n - 1) + fibonacci_rec(n - 2)


def fibonacci_iter(n):
    if n == 0:
        return 1
    if n == 1:
        return 1

    prev = 1
    curr = 1

    while n - 1:
        swap = curr
        curr += prev
        prev = swap
        n -= 1
    return curr
