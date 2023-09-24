# **Find Cost of Tile to Cover W x H Floor** - Calculate the total cost of tile
# it would take to cover a floor plan of width and height, using a cost entered by the user.

def cost(w, h, c):
    return w * h * c


w = int(input("Enter width: "))
h = int(input("Enter height: "))
c = int(input("Enter cost: "))
print(cost(w, h, c))