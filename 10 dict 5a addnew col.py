import numpy as np
# create a new col
mydict = {
'Name': ['Anastasia', 'Anastasia', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'City': ['California', 'Los Angeles', 'California', 'California', 'California', 'Los Angeles', 'Los Angeles', 'Georgia', 'Georgia', 'Los Angeles'],
'Salary': [2000, 3000, 44000, 5000, 6000, 7000, 8000, 9000, 10000, 11000],
'Year': [2020, 2019, 2018,2020, 2019, 2018,2020, 2019, 2018,2020],
'Job Title':['Manager','Director','Sales Person','Manager','Director', None,None,None,None,None],
'Age':[21,21,31,21,31,46,21,38,49,31]
}

mydict['NewCol'] = list ( np.zeros(10) ) 
print ( mydict )

for i in range ( len(mydict['Salary'])):
    mydict['NewCol'][i] = mydict['Salary'][i] * 2
#print ( mydict)        

#
#print ( np.array( mydict['NewCol']).sum()) 