# **Fibonacci Sequence** - Enter a number and have the program generate the Fibonacci sequence to that number or to the Nth number.

def fib_to_n(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    else:
        return fib_to_n(n-1) + fib_to_n(n-2)


print(fib_to_n(20))
