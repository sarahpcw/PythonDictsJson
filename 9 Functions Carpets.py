#Exercise carpet quote
"""
Create 4 functions:
1.
Name of the function: 	printCompanyMessage
Input parameters:  	  none
What to do: 		      print a  message : "Welcome to ABC Carpets!"
Return value: 		none	
2.
Name of the function: 	printPersonalGreeting
Input parameters  	firstname  
What to do: 		    Print a personalised message: "thank you", firstname, " for requesting a quote" 
Return value: 		none
3.
Name of the function: 	 calcArea
Input parameters:  	 length and width
What to do: 		     create a value area by multiplying the length and width and print this value
Return value: 		 area
4.	
Name of the function: 	 calcPrice  
Input parameters:  	 area
What to do: 		 multiply the area with the sqm price of a carpet (15 Pounds) and add the vat of 20%
        ,  print this price
Return value: 		none

#ask the end user his name
#ask the end user the length and width of a room
call the printCompanyMessage to print the company welcome message
call the function printPersonalGreeting to greet and thank the user
call the function calcArea to calculate the area of a carpet
call the function calcPrice to calculate and print the quoted price for the carpet


""" 
# carpet quotes 
# executing file
#################
# STEP 1: from file import class 
# Step 2: create an object, myareas is the object name
# object is a memory resident copy of the class
#################
# Step 3 : prefix all the function calls with the object name

from areasvat import areasvat
myarea = areasvat()  

myarea.printCompanyMessage()  
firstname = input("Please enter your name")
myarea.printPersonalGreeting(firstname)
w = float ( input ("What is the width?" ) )
l = float ( input ("What is the length?") )
a = myarea.calcArea (l,w) # + - * / ()
carpetprice = myarea.calcPrice (a)
myvatprice  = myarea.calcvat(carpetprice)
print (myvatprice)








