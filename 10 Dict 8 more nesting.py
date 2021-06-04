people = {'emp1': {'name': 'John', 'age': '27', 'gender': 'Male', 'Hobbies': {'Sport':'Running', 'Games':'Chess'}},
          'emp2': {'name': 'Marie', 'age': '22', 'gender': 'Female', 'Hobbies': {'Sport':'Swimming', 'Games':'Chess'}} ,
          'emp3': {'name': 'Peter', 'age': '29', 'gender': 'Male', 'married': 'Yes'} ,
          'emp4': {'name': 'Peter', 'age': '29', 'gender': 'Male', 'married': 'Yes', 'Hobbies': {'Reading':'Crime' }}}
 

#print (people[1]['Gender']['f']) """

print ( '--lengths--')
print ( len (people))
print ( len (people['emp4']))
print ( len (people['emp1']['name']))
print ( len (people['emp1']['Hobbies']))

print ( '--values--')
print ( people['emp1'])
print ( people['emp1']['name'])
print ( people['emp1']['Hobbies'])
print ( people['emp1']['Hobbies']['Games'])

print ( '--keys--')
print ( people.keys())
print ( people['emp1'].keys())
print ( people['emp1']['Hobbies'].keys())

print ( '-- loop and nested loop to print all dicts--')
for key, innerdict in people.items():
    print ( key )
    for key2, value in innerdict.items():
#        print ( key2, value)
        if type( value ) == dict:
            print ( key2, ':', end=" ")
            for k,v in value.items():
                print (k,'=',v, end=", ")
#        else: 
#            print ( key2, value)
    print ( '')
    
    
    
    
    
    
    
    

