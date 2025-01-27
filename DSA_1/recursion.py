"Factorial"

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))


"Fibonacci"

def fibonacii(n):
    if n <= 1:
        return n
    return fibonacii(n - 1) + fibonacii(n - 2)

print(fibonacii(6))


"Sum of digits"

def sum_of_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_of_digits(n // 10)

print(sum_of_digits(12345))