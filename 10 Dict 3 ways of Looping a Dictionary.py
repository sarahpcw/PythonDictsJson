# -*- coding: utf-8 -*-
"""
Looping over dictionary
"""
#creating a dictionary
bikes = {"Royal_Enfield":"Continental","Kawasaki":"Ninja","Yamaha":"R1"}
print (bikes["Royal_Enfield"])

print (bikes.keys())
#Iterating over the dictionary to print keys
print ('Keys are:')
for key in bikes.keys():
  print (key)

#Iterating over the dictionary to print values
print ('Values are:')
for models in bikes.values():
  print(models)
print( bikes.values() )

#Iterating over the dictionary to print values
print ('Key, Values pairs are:')
for key, value  in bikes.items():
    if key =="Yamaha":
        print(key , '++>', value)
  
print ( bikes.items() )