
# **Next Prime Number** - Have the program find prime numbers until the user chooses to stop asking for the next one.

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if not n & 1:
        return False
    for x in range(3, n // 2 + 1, 2):
        if n % x == 0:
            return False
    return True


def next_prime(n):
    while not is_prime(n):
        n += 1
    return n


oui = 2
while True:
    oui += 1
    oui = next_prime(oui)
    print(oui)
    sl = input('Continue? [anything for Y/n for stop] ')
    if sl.lower() == 'n':
        break
