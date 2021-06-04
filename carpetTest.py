from cfPerCountry import cfPerCountry   # from filename import classname
import math
#from carpetFunctionDefinitions import carpetFunctionDefinitions  # from filename import classname
print( __name__ )
print ( math.sqrt(100))
 

c = cfPerCountry("abc Carpets", "xyz carpets",0.99)     # create an object using the classname
                                                     # prefix all function calls with the object name
print ( c.sqrt(100) ) 

area = c.calcArea(10,20)
c.printCompanyMessage()

print ( "Area", area )

if area > 1000 :
    print ( "Too big for us, sorry!")
elif area < 5:
    print ( "Too small for us, sorry!")
else:
    cp = c.calcPrice(area)  ## which version of calcprice is used : the one in the child (override)
    print ( cp)
    c.calcVat(cp)

a = 100
c.seta()
print (c.geta())
x = c.geta()
print ("the end", x)




#### Creating the execution class
# from filename import classname
# create class ( classname of the imported class in the brackets )
# indent all code
# create an object using the classname
# prefix all function calls with the object name


 
""" inheritance: 
    parent and child class
    the child import the parent class
    the run or execution class instantiates the child class
    the child class collects the parameters for the constructor of the parent 
    and supplies it to the parent with the super key word.
    self. extends the scope of a variable, making the variable visible in all functions of the class  """
    
    
    
    