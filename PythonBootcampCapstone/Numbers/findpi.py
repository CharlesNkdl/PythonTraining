# **Find PI to the Nth Digit** - Enter a number and have the program generate &pi; (pi)
# up to that many decimal places. Keep a limit to how far the program will go.

import math
def findpi(n):
    return round(math.pi, n)


print(findpi(15))