from nesteddicts import dictFunctions
class runNestedDicts(dictFunctions):
    peopleDict = {'emp1': {'name': 'John', 'age': '27', 'gender': 'Male'},
                  'emp2': {'name': 'Marie', 'age': '22', 'gender': 'Female'} }
    
    # peopledict.keys() vs peopledict['emp1'].keys() 
    # len(peopledict['emp1']) vs len(peopledict)
    
    obj = dictFunctions()         # create details
    
    obj.getInfo(peopleDict)       #info about the entire dict
    
    obj.getPersonInfo(peopleDict) #info about the outerkeys (emp1 only) 
#    
#    # refer to individual values
    obj.getDetails(peopleDict)    # info about the value of an outerkey
#    
    obj.addelements(peopleDict)   # emp3 and emp4   - adding a new key, value pair to the OUTER dict
    obj.addetails(peopleDict)     # hobbie for emp4 - adding a new key, value pair to the INNER dict
    obj.updatedetails(peopleDict) # change/update emp3 and del gender of emp2
    
    obj.addsalaries(peopleDict)
    
    obj.iterateDetails(peopleDict)
    
    obj.sumsalaries(peopleDict)
    
    obj.gettypes(peopleDict)       # emp1 <class 'dict'>
#    

#    
    




 
