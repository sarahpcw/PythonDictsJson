# 1. create a class: class classname:
# 2. indent all functions
# 3. use the self parameter , 1st parameter in every function

# function library
class carpetfunction: 
    def __init__(self, p):
        self.p = p
        
    def printCompanyMessage(self):
        print ( "Welcome to ABC Carpets!" )
    
    def printPersonalGreeting(self,firstname):
        print ( "Hi,", firstname.title(), ", thanks for requesting a quote!" )
        
    def calcArea(self,l,w):
        area = l*w
        print ( "The Area is (Parent class): ", area )
        return area
    
    def calcCarpetPrice(self, area):
#        sqm_price = 15    # get the sqmprice as a instance parameter
        carpetprice = area * self.p  # * sqm_price
        print ( "Carpet Price (Parent class):", "%.2f" % carpetprice)
        return carpetprice
 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
#    def __init__(self, sqm_p, labourprice):
#        print ("Constructor of Parent Class")
#        self.sqm_price =sqm_p
#        self.labour_price = labourprice
#    def setFirstName (self):
#        firstname = input("Please enter your name: ")
#        self.firstname = firstname
#    
#    def setWidth (self):
#        w = float ( input ("What is the width?" ) )
#        self.w = w
#    
#    def setLength(self):
#        l = float ( input ("What is the length?") )
#        self.l = l
#        
#    def getFirstName (self):
#        return self.firstname
#    
#    def getWidth(self):
#        return self.w
#
#    def getLength(self):
#        return self.l
##    using self.LabourPrice i.e. instance / object variable set in __nint__
#    def calcCarpetLabourPrice (self, area):
#        LabourCarpetPrice = area * self.labour_price 
#        print ( "Labour Price to fit the carpet (Parent class): ", "%.2f" % LabourCarpetPrice)
#       
#
##    using self.LabourPrice i.e. instance / object variable set in __nint__    
#    def calcRemovalLabourPrice (self, area):
#        RemovalLabourPrice = area * self.labour_price 
#        print ( "Labour Price removing old carpet (Parent class): ", "%.2f" % RemovalLabourPrice)
#        
#    
##    using self.LabourPrice i.e. instance / object variable set in __nint__
#    def calcCleaningLabourPrice (self, area):
#        CleaningLabourPrice = area * self.labour_price 
#        print ( "Labour Price (Parent class): ", "%.2f" % CleaningLabourPrice)
#         