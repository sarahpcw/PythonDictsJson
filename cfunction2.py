from cfunctions import cfunctions
class cfunctions2 (cfunctions):
    def __init__(self, name):
        super().__init__(name)  # provides the parameters required by the init function of the parent class
        self.name = name
        self.count = 0
        cfunctions2.count = 0
        
            
    def listHobbies ( self,  *hobbies ) :
        print (self.name)
        for hobby in hobbies :
            print ( 'Your Hobby is', hobby)
    
    def calcPrice (self, area):
        sqm_price = 15
        carpetprice = area * sqm_price * 2.5
        return sqm_price,  carpetprice
    
    def countquotesCustomer ( self  ):  ## 2 different 
        self.count +=1
        return self.count
    
    def countquotesAll ( self  ):  ## both object will access this variables
        cfunctions2.count +=1
        return cfunctions2.count
    
    
        