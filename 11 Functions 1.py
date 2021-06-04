##### all function definitions
def calcarea( length, width = 2):  		#defining a function
    area = length * width
    print ("The area is" ,area)
    
def substract1( a, b ):  		#defining a function
    aminusb = a - b
    print ("The area is" ,aminusb)

def LargestNumb( a, b ):
    if a > b:
        print (a, "is  bigger  ")
    else: 
        print (a, "is smaller")

def LargestNumb2( a, b ):
    largest = 0
    if a > b:
        largest = a
    else: 
        largest = b
    return largest

def calcproduct( length, width = 2 , depth = None): #default values, depth optional
    if depth == None : 
        area = length * width 
    else: 
        area = length * width + depth
    print ("The area is" ,area)

calcproduct(length = 7, width = 2 , depth = 3)
calcproduct(7,2,3) 
calcproduct(7, 3) # matches length and width
calcproduct(7, depth = 3) # matches length and depth
calcproduct( width = 7, depth = 3) # supplying length is compulsory




LargestNumb(7,5)
l = LargestNumb2( 7,5)
print (l, " is bigger" )


#### the main flow of the program
print ( '---' )
substract1( b=2, a=10)
substract1( 10, 2 )
substract1( 2, 10)


""" create a function
input parameters : a , b
find out which value is bigger
return the biggest number

"""
