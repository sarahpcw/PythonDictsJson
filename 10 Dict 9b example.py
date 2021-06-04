# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 15:44:39 2020

@author: u
"""

mydict = {
    "glossary": {
        "title": "example glossary",
		 "GlossDiv": {
            "title": "S",
			   "GlossList": {
                "GlossEntry": {
                    "ID": "SGML",
					"SortAs": "SGML",
					"GlossTerm": "Standard Generalized Markup Language",
					"Acronym": "SGML",
					"Abbrev": "ISO 8879:1986",
					"GlossDef": {
                        "para": "A meta-markup language, used to create markup languages such as DocBook.",
						"GlossSeeAlso": ["GML", "XML"]
                    },
					"GlossSee": "markup"
                }
            }
        }
    }
}
                    
                    
print ( type( mydict['glossary']) )

for key, a in mydict.items():
    print (key)
    if type(a) == dict:
        print ( a.keys())
        for k1 , b in a.items():
            if type(b) == dict:
                print (k1, b.keys())
                for k2 , c in b.items():
                    if type(c) == dict:
                        print (k2, c.keys())
                        for k3 , d in b.items():
                            if type(d) == dict:
                                print (k3, d.keys())
                                for k4, e in d.items():
                                    if type (e) == dict:
                                        print ( k4, e.keys())
                    
               
        
