"""
class movieFunctions:
    tp = 0
    def __init__(self, price):  # price is a parameter of init
        self.tp = price
"""

from popcorn import popcorn  

m = popcorn(10)

movie = 'bambi'

a, p, c = m.askTicketNumbers()

TotalPrice = m.calcTp(a,p,c)

popcorn =  m.calcPopcorn(  a , p , c) 

m.printTickets( movie, a, c, p, TotalPrice)
print ( 'popcorn ', popcorn)
print ( 'TotalPrice with popcorn ', (popcorn+TotalPrice))