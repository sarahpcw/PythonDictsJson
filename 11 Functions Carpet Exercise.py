# 1. from filename import classname
# 2. create class
# 3. indent everything below the class name
# 4. create object
# 5. prefix all function calls with object name

from carpetfunction  import carpetfunction 

obj=carpetfunction ()   
# create an object, create an instance , instantiate
# __init__ is run when object is created
# 15 is the carpetprice per square meter, and 2 is the labourprice per sq meter

obj.printCompanyMessage() 

firstname = input("Please enter your name")
obj.printPersonalGreeting(firstname)

w = float ( input ("What is the width?" ) )
l = float ( input ("What is the length?") )

a = obj.calcArea (l,w) # + - * / ()

obj.calcCarpetPrice (a)


    






    
    
    
    
    
    #ask the end user the length and width of a room
    #ask the distance of travel
#Call calcArea and get the return value, area
#Call calcCarpetPrice and get the return value, carpetprice
#Call calcTravelFee and get the return value, travelfee
#Call printCarpetCost  

