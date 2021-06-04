# Add , delete and update values
 
# declare and initialise a dictionary
people = {'emp1': {'name': 'John' , 'age': 27  , 'gender': 'Male'},
          'emp2': {'name': 'Marie', 'age': 22, 'gender': 'Female'} }
print (len(people)) 
print (len(people['emp1']))
print (len(people['emp2']))
print (people['emp2'])

# Add a new key value pair
people['emp3'] = {'name': 'Peter', 'age': 28, 'gender': 'Male', 'married': 'Yes'}
# Add a new key value pair
people['emp4'] = {'name': 'Paul',  'age':31, 'gender': 'Male', 'married': 'No'}

people['emp3']['surname']="Jones"
print (people['emp3'])

people['emp3']['Hobbie']={"hobbie1": 'Swimming', "hobbie2": 'Reading'}
print (people['emp3'])

print ()
#  what is the average age
#  get the total and divide it by the len(people) 
print (people['emp1']['name']) 
print (people['emp3']['Hobbie']['hobbie1']) 
myage = 0 
count = 0
for key, value in people.items():
    print ( key )
    for k,val in value.items():
        print ( '  ', k, ' --- ' , val)
        if k == 'age' :
           myage = myage + val
           count += 1
print ( 'Average age' , (myage / count )) 

myvalue = max( each['age'] for each in people.values() ) #if each) 
print ( 'myvalue ' , ( myvalue ) )


print (len(people['emp3']))
print (len(people['emp4']))

print ( people )
print ( people['emp1']['name'])
print  (people['emp2']['name'])
print (people['emp3']['name'])
print (people['emp4']['name'])

print (people.keys())
print ( people['emp1'].keys())
print ( people['emp4'].keys())


print("people[emp3]",people['emp3']) 

print ('Key, Values pairs are:')
for key, value  in people.items():
  print(key , '++>', value)

for key, innerdict in people.items():
    print ( key )
    for k,val in innerdict.items():
        print(k , '++>', val)
        if k == 'Hobbie':
            print ( )
    print ( "" ) 
    
#add
people['emp3']['Hobbie']={"hobbie1": 'Swimming', "hobbie2": 'Reading'}
# refer to a specific key
print("people[emp3]",people['emp3'])

for key, innerdict in people.items():
#    print ( innerdict )
    for k,val in innerdict.items():
        if type(val) == dict :
            print ( val.values() )
    print ( "" ) 

# referring to values
print ( people['emp3']['married'])
print ( people['emp1']['age'])
print ( people['emp4']['Salary'])
# referring to values
print ( people['emp3']['Hobbie'])




## updating 
print ( people['emp3']['name'])  
people['emp3']['name'] = 'Luna'
print ( people['emp3']['name'])  
## updating 
people['emp3']['age'] = '24'
people['emp3']['gender'] = 'Female'
people['emp3']['married'] = 'No'
print("people[emp3]",people['emp3'])

# Delete
del people['emp3']['gender']
print("people[emp3]",people['emp3'])

#### add a value for all
for key, value in people.items():
    people[key]['Salary'] = 100
print (people.values())
## iterate to view the values
s = 0; 
for key, innerdict in people.items():
    print ( key, '---')
    for k, value in innerdict.items():
        if 'Salary' == k:
            s += value
print ("total salaries", s)
 
sumValue2 = sum(each['Salary'] for each in people.values() ) #if each) 
print ("\nsum of all the salaries",sumValue2)

 
# get info
print ( len (people))
print ( people.keys())
print ( people.values())
print ( people.items())

# iterate the dictionary
for key, val in people.items():
    print (key)
    print ( val.keys() ) 
    for k, value in val.items():
        print ( k , '==>', value)
