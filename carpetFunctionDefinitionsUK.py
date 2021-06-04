# all function definitions, indented
# class name
# self as first parameter in all functions

### child class
from cf import cf  ## extends
class carpetFunctionDefinitionsUK(cf):
    
    def __init__(self,  price, c ):  # parametized constructor
        super().__init__(price = price, city = c)
        print ("Welcome to", c)
        self.sqm_price = price
        
#    
    def calcprice (self, area):             # input parameter but no return value
        carpetprice = area * self.sqm_price  *  2
        print ( "Carpet price", "$%.2f" % carpetprice)
        return carpetprice
    
    def calcVat (self, cprice):
        cp = cprice* 1.2
#        print ( self.sqm_price )
        print ("Carpet price including VAT", "$%.2f" % cp) 
        