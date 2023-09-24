
# **Prime Factorization** - Have the user enter a number and find all Prime Factors (if there are any) and display them.
def primefactor(n):
    while n % 2 == 0:
        n = n / 2
        print(2)
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            n = n / i
            print(i)
    if n > 2:
        print(n)


primefactor(514)