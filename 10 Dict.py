#Do you just need an ordered sequence of items? Go for a list.

#Do you need to associate values with keys, 
#   so you can look them up efficiently (by key) later on? Use a dictionary.
from dictFunctions import dictFunctions

class dicts (dictFunctions):
     
    mydict = {'Name': 'Zara'  , 'Age': 7 , 'Subject': 'Maths'}
    
    obj = dictFunctions()
#    
#    obj.print_dict(mydict)      # print all of it
#       
#    obj.change_dict(mydict)     # change the dict
##
    obj.print_selected(mydict)   # print selected values from the dict, using selected keys
##    
#    obj.change_dict_del(mydict) # delete a key value pair from a dictionary
##    
    obj.dict_functions(mydict)   # dict BUILT_IN functions #.keys()  .values() .items()   sorted  len
##        
    v = obj.iterate_dict(mydict) # iterate over all key, value pairs
    print (v)
##        
    obj.sort_dict(mydict)        # sort by key 
#
    obj.dump_to_file( mydict)    # put mydict dictionary into people file as json format
##    
    mydict = obj.load_from_file()
    print ('Final ----------', mydict )
##    
    myvar = 'Name'
    obj.find_value(mydict, myvar)
#
#    x = None
#    print ( type(x))
    
