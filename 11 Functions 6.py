# multiple return values
def f1 ():
    a = 10
    b= 11
    c = 12
    return a,b,c

# multiple input parameters
def f2 (name, *hobbies):
    print ( name.title() , end = (" ") )
    if len(hobbies)>=1 :
        print  ( 'has the following hobby(ies):')
        for h in hobbies:
            print (h)
    else:
        print ( 'has no hobbies ')
    print ( '\n')

# optional parameters
def f3 (name, hobbies='swimming', handbag='Armani'):
    print ( 'Name: ' ,name)
    if hobbies != None:
        print ('Hobby: ', hobbies)
    if handbag != None:
        print ('Handbag: ', handbag)
    print ( '\n')     

def subtract ( a,b ):
    sums = a-b
    return sums
print ( subtract ( 5 , 10)  )
print (subtract ( 10, 5) )
print (subtract ( b = 5,  a = 10) )
###### execute the functions

#adult, child, pensioner = f1()
#f2 ('mike')
#f2 ('mike')
#f2 ('john', 'swimming', 'reading')
#f2 ('peter', 'swimming', 'reading', 'movies')
#
##
###
#f3 ('mary')
#f3 ('sally')
f3 ( name = 'annie')
##
#
#
