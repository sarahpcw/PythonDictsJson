# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 16:07:40 2020

@author: u
"""

mydict = { 
    "window": {
        "title": "Sample Konfabulator Widget",
        "name": "main_window",
        "width": 500,
        "height": 500
    },
    "image": { 
        "src": "Images/Sun.png",
        "name": "sun1",
        "hOffset": 250,
        "vOffset": 250,
        "alignment": "center"
    },
    "text": {
        "data": "Click Here",
        "size": 36,
        "style": "bold",
        "name": "text1",
        "hOffset": 250,
        "vOffset": 100,
        "alignment": "center",
        "onMouseUp": "sun1.opacity = (sun1.opacity / 100) * 90;"
    }
}   

# what is the length of the dictionary
print ( len( mydict) )   # 3
# what is the keys of the dictionary
print ( mydict.keys())
# print the keys for mydict['window']
print ( mydict['window'].keys())

# write the dictionary to a json file
import json
with open('newjason.json', 'w') as myFile: 
    json.dump(mydict, myFile) 

# print all the keys , loop the innerdict and print key and values
for key, val in mydict.items():
    print ( '---',key)
    for  k, v    in val.items():    
        print ( k,v)
        
# print all the keys , loop the innerdict and in a png filename is found, print key and values    
for key, val in mydict.items():
    print ( '----', key)
    for k,v in val.items():
        if  'png' in str(v) :
            print ( k, v)
            
            
            