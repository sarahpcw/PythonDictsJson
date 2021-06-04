# sum the salaries
# declare and initialise a dictionary
people = {'emp1': {'name': 'John' , 'age': '27', 'gender': 'Male'},
          'emp2': {'name': 'Marie', 'age': '22', 'gender': 'Female'} ,
          'emp3': {'name': 'Peter', 'age': '28', 'gender': 'Male', 'married': 'Yes'},
          'emp4': {'name': 'Peter', 'age': '29', 'gender': 'Male', 'Hobbies': "running"}}
   
print(people['emp4']['age'])
print(people['emp1'])

print (len(people['emp1']))  #len of the innerdictionary Value of emp1
print (len (people))

for key, value  in people.items():
        print(key , '---', value)

for key ,  value in people.items(): 
    print(key, 'length',len(key))
    for k , v in value.items():
        print ( '    ',  k ,' --- ' ,v)

people['emp1']['Salary']  = 55
people['emp1']['Pet']     = 'hamster'
print(people['emp1'])

for key, value in people.items():
    people[key]['Salary'] = 100
    
for key, value  in people.items() :
        print(key , '---', value)
#        print (value.keys())
## iterate to view the value
#
people['emp1']['Salary'] = 55
people['emp3']['Salary'] = 555

maxSalary = max( each['Salary'] for each in people.values() ) #if each) 
print ("MAX of all the salaries", maxSalary )

minSalary = max( each['Salary'] for each in people.values() ) #if each) 
print ("MAX of all the salaries", minSalary )

sumValue2 = sum( each['Salary'] for each in people.values() ) #if each) 
print ("SUM of all the salaries", sumValue2 )

del people['emp4']['Salary']
print ( people['emp4'])

sumValue=0
for key ,  value in people.items(): 
    if 'Salary' in value.keys():   #    if value and 'Salary' in value.keys(): 
        sumValue = sumValue +  value['Salary']  
print ( "sumValue",sumValue)



#