# **Mortgage Calculator** - Calculate the monthly payments of a fixed term mortgage over given Nth terms at a
# given interest rate. Also figure out how long it will take the user to pay back the loan. For added complexity,
# add an option for users to select the compounding interval (Monthly, Weekly, Daily, Continually).

def mortgage(p, r, n):
    r = r / 100
    m = p * (r * (1 + r) ** n) / ((1 + r) ** n - 1)
    print("Annual payment: ", round(m, 2))
    print("Monthly payment: ", round(m/12, 2))
    print("Weekly payment: ", round((m/12)/30 * 7, 2))
    print("Daily payment: ", round((m/12)/30, 2))
    print("Total payment: ", round(m * n, 2))


p = int(input("Enter principal: "))
r = float(input("Enter interest rate: "))
n = int(input("Enter number of payments: "))
mortgage(p, r, n)
