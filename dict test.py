import json

mydict = {'Name': 'Zara Blue'  , 'Salary': 7000 , 'Age': 21}
mydict['School'] = "DPS School"; # Add new entry

for key, val in mydict.items():
    if 'Name' in key :
        print ( val[0:10])
        mylist = mydict[key].split(' ')
        print ( mylist)
        print (mylist[0], mylist[1], mylist[4])
    if 'Salary' in key:
        mydict[key]= 5557

print ( mydict.values())
 
with open('newjason.json', 'w') as myfile:
   json.dump(mydict , myfile) 		
