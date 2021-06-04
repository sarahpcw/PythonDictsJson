# order of parameters
def subtract ( a, b):
    sums = a-b
    return sums
###### execute the function
print ( subtract ( 5 , 10)  )
print ( subtract ( 10, 5) )
print ( subtract ( a = 10, b = 5) )
print ( subtract ( b = 5, a =10) )


# multiple return values
def f1 ():
    a = 10
    b = 11
    c = 12
    return a,b,c

adult , child , pensioner = f1()
print ( adult , child , pensioner )



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



#f2 ('mike')
f2 ('mike')
f2 ('john', 'swimming', 'reading')
f2 ('peter', 'swimming', 'reading', 'movies')






# optional parameters
def f3 (name=None, hobbies='swimming', handbag=None):  #specify defaults, which will be used if not value passed is in
    print ( 'Name: ' ,name)
    if hobbies != None:
        print ('Hobby: ', hobbies)
    if handbag != None:
        print ('Handbag: ', handbag)
    print ( '\n')     
#
##
###
f3 ('mary')
f3 ('sally', 'Reading')
f3 ( 'sally', 'Reading','Gucci')
f3 ( handbag='Gucci')
f3 ( 'Gucci')
f3 ( 'Reading')

##
#
#
