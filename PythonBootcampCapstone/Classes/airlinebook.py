# **Airline / Hotel Reservation System** - Create a reservation system which books airline seats or hotel rooms.
# It charges various rates for particular sections of the plane or hotel.
# Example, first class is going to cost more than coach.
# Hotel rooms have penthouse suites which cost more. Keep track of when rooms will be available and can be scheduled.

import random
class AirlineReservation:
    def __init__(self):
        self.curr_price = random.randint(10, 50)
        self.first_class = 0
        self.dest = ""
        self.destprice = 0

    def desti(self, destination):
        self.dest = destination
        self.destprice = (ord(destination[0]) * self.curr_price) * (1 + int(self.first_class))
        print("Your destination is %s" % self.dest)
        print("Your price is %s" % self.destprice)

    def first_class(self):
        self.first_class = 1
        print("You have chosen first class")


air1 = AirlineReservation()
d = 'New York'
air1.desti(d)






