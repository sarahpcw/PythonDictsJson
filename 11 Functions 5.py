def calcC ():
    a = 10 
    b = 20
    c = 30 
    return a,b,c  # 3 return values

def printHobbies(name,  *hobbies):
    print ('--name', name)
    mylist = list(hobbies)
    print ( type(hobbies) , type(mylist))
    for hobby in mylist: 
        print ( hobby )



x , y, z = calcC ()  # 3 return values

print ( x , y, z )



printHobbies('John',  'swimming', 'Reading') 
printHobbies('Peter', 'a', 'b', 'c') 
printHobbies('Paul', 'Reading', 'Swim', 'Run') 
printHobbies('Mike', 'manager', 'Reading','Cards', 'Movies', 'Cooking', 'walking') 


