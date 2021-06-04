# listing all functions, functions library
# create a class with a class name
# use the self keyword as the first parameter in all the functions 
########## functions

from carpetfunction import carpetfunction  #super , parent , base class

class cf (carpetfunction):  # sub or child
    def __init__(self, lp, p):
        self.lp=lp
        self.p =p
        super().__init(p)
        
    def calcArea(self, l , w ):       # override (function in child overrides function in parent)
        area = l*w * 1.05
        print ('Area * 1.05 (child class): ', area)
        return area
    
    def calcCarpetLabourPrice(self, a):
        fittingcost = 10
        return a * self.lp * fittingcost
    
    def calcRemovalLabourPrice(self, a):
        rcost = 5
        return a * self.lp * rcost
    
    def calcCleaningLabourPrice(self, a):
        clcost = 20
        return a * self.lp * clcost

    def printFinalMessage(self):
        print("thank you, the end")