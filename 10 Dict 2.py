#Dictionary functions
#   dict = {'Name': 'Zara', 'Age': 7};
#   print (“dict converted to string : ”, repr(dict) ) 	#This method returns string representation.
#Dictionary functions 
#Clear, del, type, len

name = 'john'
mydict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

print ( len (mydict) )  	
print(mydict)

print(  mydict['Name'] )    # mylist[0]
print(  mydict['Age']  )  
print(  mydict['Class'])  	


print ( mydict.keys()   )
for key in mydict.keys():
    print ( key )
 
print ( mydict.values() )
for each in mydict.values():
    print ( each)
    
print ( mydict.items()  )
for key, value in mydict.items():
 	 print (key, "=>", value)



mydict['School'] ='Abc School'
print (mydict)
print ( len (mydict) )  	
print(mydict)


mydict.clear();  
   						# remove all entries in dict
print ( mydict)

for key,val in mydict.items():
 	 print (key, "=>", val)

del mydict ;
print ( mydict)        						# delete entire dictionary
#for key,val in mydict.items():
# 	 print (key, "=>", val)
#      
      
mydict = {'Name': 'Zara', 'Age': 7};
print ("Variable Type : %s" %  type (mydict))		# returns  the type
print ("Length : %d" % len (mydict))  			# returns  the length of dict


