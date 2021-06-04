# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 22:04:01 2020

@author: u
"""
mydict = {
  "items": [
    {
      "id": "12345",
      "links": {
        "self": "https://www.google.com"
      },
      "name": "beast",
      "type": "Device"
    }
  ],
  "links": {
    "self": "https://www.google.com"
  },
  "paging": {
    "count": 1,
    "limit": 1,
    "offset": 0,
    "pages": 1
  }
}
  
print ( len ( mydict))
print ( mydict.keys())
for k,v in mydict.items():
    print ( k , type (v))
    if type(v) == dict:
        print ( '--',v.keys())
    
