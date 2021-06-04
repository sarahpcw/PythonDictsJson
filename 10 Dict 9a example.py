# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 22:24:29 2020

@author: u
"""
import json
with open('socrata_metadata.json') as peopleFile:
  mydict = json.load(peopleFile) 

print ( len (mydict ))
print ( mydict.keys())
print ( len ( mydict.keys()) )
print ( mydict['tags'])
#
for key, val in mydict.items():
    print (key , '===>' , type(val) )
#
#print ( mydict) 
#
#myfile = open ()