# -*- coding: utf-8 -*-
 

###################################################################
##Replicate a dictionary, changing it to string
#print('')
dicta = {'name': 'Peter', 'age': '29', 'Gender': 'Male', 'married': 'Yes'}
dictb = repr(dicta)
print ("dictb\n",type(dictb), dictb [0:10])  # MAKES IT INTO A STRING
print ("dictA\n",type(dicta), dicta)


