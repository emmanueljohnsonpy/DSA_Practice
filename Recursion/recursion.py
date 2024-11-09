# Factorial


def factorial(n):
    if n==1 or n==0:
        return 1
    return n * factorial(n-1)

res=factorial(5)
print(res) 


# Fibonacci series


def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

res=fibonacci(6)
print(res)


# Sum of list

def sum_of_list(lst):
    if not lst:
        return 0
    return lst[0]+sum_of_list(lst[1:])

lst=[1, 2, 3, 4, 5]
res=sum_of_list(lst)
print(res) 


# Sum of digits

def sum_of_digits(n):
    if n==0:
        return 0
    return n%10 + (sum_of_digits(n//10))

res=sum_of_digits(12345)
print(res) 