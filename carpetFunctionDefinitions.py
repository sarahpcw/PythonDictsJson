# all function definitions, indented
# class name
# self as first parameter in all functions


### parent / base class
class carpetFunctionDefinitions:
    
    def __init__(self,  coname, sqm_price, ):
        self.sqm_price = float ( sqm_price ) 
    
    def printwelcome(self): 
        print ( "Welcome to ABC Carpets!" )   # no input parameter and no return value
        
    def carpetinfo (self, msg):               # input parameter
        info  = input(msg)
        info  = float(info)
        #width = int(width)
        print ("", info)  
        return info   # return value
    
    def carpetlengthWidth (self):               # input parameter
        w = input ( "What is the width ")
  
        l = float ( input ("Give me the length of your carpet") ) 
        
        print ("length ", l, "width" , w)  
        return w, l  # two return values
    
    def calcprice (self, area):             # input parameter but no return value
        carpetprice = float( area ) * self.sqm_price * 1.09
        print ( "Carpet price", "$%.2f" % carpetprice)
