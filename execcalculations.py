from calculations import calculations

c = calculations(99)   # create an object of the class calculations
## here the __init__ runs automatically
# init runs when I create the object
# I cannot call the init function
# if the init function has an input parameter, then i supply
# its value when creating the object

v = c.calcValue()

c.printvalue(v)

v = c.calcValue2()

c.printvalue(v)