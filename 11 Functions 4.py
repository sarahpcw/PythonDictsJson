def printfirst():  		#defining a function
   print ("hello world")
   
def printme( strvar ):
   print ( strvar )
 
def giveme():  
    strvar= "The Wolf of Wall Street"
    return strvar;

def concatme( str1, str2):
   strvar = "hello "+ str1  + ' ' + str2
   return strvar; 


# Now you can call  or execute the functions
printfirst ()  			# gets nothing, returns nothing

printme ("Mississippi") 	# gets something, returns nothing
printme ("Kilimanjaro")

a = giveme() 				# gets nothing, returns something
print (a)
 
a = concatme( "world" , "and sun") 	# gets something and returns something
print (a)