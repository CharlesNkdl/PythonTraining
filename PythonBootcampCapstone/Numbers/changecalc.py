# **Change Return Program** - The user enters a cost and then the amount of money given. The program will figure out
# the change and the number of quarters, dimes, nickels, pennies needed for the change.

def changecalc(cost, money):
    if money < cost:
        print ("You don't have enough money")
    elif money == cost:
        print ("You don't need change")
    else:
        change = (money - cost)
        quarters = change // 0.25
        change = change % 0.25
        dimes = change // 0.10
        change = change % 0.10
        nickels = change // 0.05
        change = change % 0.05
        pennies = change // 0.01
        print (f"quarters: {quarters} dimes {dimes} nickels {nickels} pennies {pennies}")


cosst = int(input("Enter cost: "))
mosney = int(input("Enter money: "))
changecalc(cosst, mosney)
