from cf import cf

obj=cf(12, 5)  
# create an object, create an instance , instantiate
# 15 is the carpetprice per square meter, and 2 is the labourprice per sq meter

obj.printCompanyMessage()  # in  parent

firstname = input ("name")  # call functions in the child class cf ( function library )
obj.printPersonalGreeting(firstname) # in  parent

w         = input ("width? ")
l         = input ("length?")
a         = obj.calcArea(l,w) # in child and parent (override) uses the version in child class

cp        = obj.calcCarpetPrice(a)  # in parent  
#
lap       = obj.calcCarpetLabourPrice(a)           
rp        = obj.calcRemovalLabourPrice(a)         
clp       = obj.calcCleaningLabourPrice(a)         
finalprice= lap + rp + clp +cp

obj.printFinalMessage()


















"""
# run setters and getters to get values of variable 
obj.setFirstName ()
obj.setWidth ()
obj.setLength ()

firstname = obj.getFirstName ()
w         = obj.getWidth ()
l         = obj.getLength ()
#obj.calcCarpetLabourPrice(a)            lp = 2.5 * fittingCost
#obj.calcRemovalLabourPrice(a)          cp = 2.5 * removalCost
#obj.calcCleaningLabourPrice(a)         cp = 2.5 * removalCost
finalprice =  
"""






