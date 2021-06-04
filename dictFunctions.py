import json  # required for loading from and dumping to file, permanent storage
class dictFunctions():

    def print_dict(self,mydict):            #print all of it
        print ( 'the whole dict:\n', mydict)
        
    def change_dict(self, mydict):          # Change the dict
        mydict['Age'] = 8                   # update existing entry
        mydict['Age'] = 8 * 2               # any arithmetic
        mydict['School'] = "DPS School"     # Add new entry
        print ( 'the whole dict after adding School:\n', mydict)
    
    def change_dict_del (self, mydict):     #delete the key,value pair
        del mydict["School"]
        print ( 'the whole dict after deleting of School:\n', mydict)
   
    def print_selected (self,mydict):       #print selected keys from the dict
        print ("The name   is ", mydict['Name'])
        print ("The age    is ", mydict['Age'])
        print ("The subject is", mydict['Subject'])
#        print ("The school is ", mydict['School'])
    
    # dict BUILT_IN functions:     #.keys()   .values()  .items()   sorted  len
    def dict_functions(self, mydict):
        print ( '----- dict_functions-----')
        print ( 'Length ',  len(mydict) )
        dictKeys = mydict.keys()
        print ( 'Keys  \n', dictKeys)
        print ( 'Values\n', mydict.values() ) 
        print ( 'Items \n', mydict.items())
    
    def iterate_dict(self, mydict):
        for  key, val  in mydict.items():    # iterate the keys and value pairs
            if "Name" in key:
                print (key,"==>", val, type(val))              
           
        for k in mydict:                     # shortcut loop for keys only
            print (k)
    
    def sort_dict(self, mydict):             # sort by key 
        for key, value in sorted(mydict.items()): ##Sorting the dictionary
            print (key, value)
    
    def dump_to_file(self, mydict):
        with open('peopleFileQWE.json', 'w') as peopleFile: 
            json.dump(mydict, peopleFile)    # put mydict dictionary into people file as json format
    
    def load_from_file(self): 
        with open('peopleFileQWE.json', 'r') as peopleFile: ##open  a json file and put it into a dictionary
               mydict = json.load(peopleFile)# use s i.e. loads when creating the dictionary from a FILE
        print ('Load from file -',mydict)
        return mydict
    
    def find_value(self, mydict, val):
        if 'School'  in mydict:
            print('found', mydict['School'])
        else:
            print ('not found')
            
        if val  in mydict:
            print('found', mydict[val])
        else:
            print ('not found')