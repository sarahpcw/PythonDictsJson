from cfunctions import cfunctions   #from filename import classname

class cfPerCountry(cfunctions): # classname   = inheritance  
    # cfunction  is the base class, superclass, parent class
    def __init__(self, name1, name2, vat):
        super().__init__( name1 )
        print ( "Welcome to ", name2, "!  Child class")
        self.vat = vat
        self.a = 0 
    
    def sqrt(self,nr):
        return nr * 1000 + 5555
    
    def calcVat ( self ,  cp ):
        finalcp = cp + ( cp * self.vat ) 
        print ( cp, self.vat, finalcp)
        return finalcp
    
    
    def calcPrice(self, area):   # override i.e. runs the child version of the function. ignores the version in the parent 
        print ( 'in child class ')
        carpetSQMPrice = 25.00
        carpetPrice = carpetSQMPrice * area
        return carpetPrice
    

    def seta (self ) :
        self.a = 10
        
    def geta (self ):
        return self.a
        