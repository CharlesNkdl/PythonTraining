# **Find e to the Nth Digit** - Just like the previous problem, but with e instead of &pi; (pi).
# Enter a number and have the program generate e up to that
# many decimal places. Keep a limit to how far the program will go.

import math

def finde(n):
    return round(math.e, n)

print(finde(15))
