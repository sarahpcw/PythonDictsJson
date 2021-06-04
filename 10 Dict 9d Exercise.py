#exercise
mydict = { 
    "window": {
        "title": "Sample Konfabulator Widget",
        "name": "main_window",
        "width": 500,
        "height": 500
    },
    "image": { 
        "src": "Images/Sun.png",
        "name": "sun1",
        "hOffset": 250,
        "vOffset": 250,
        "alignment": "center"
    },
    "text": {
        "data": "Click Here",
        "size": 36,
        "style": "bold",
        "name": "text1",
        "hOffset": 250,
        "vOffset": 100,
        "alignment": "center",
        "onMouseUp": "sun1.opacity = (sun1.opacity / 100) * 90;"
    }
}   
 

#### Question 1
# what is the length of the dictionary

# what is the keys of the dictionary

# print the keys for mydict['window']


#### Question 2
# write the dictionary to a json file
 

#### Question 3
# print all the keys , loop the innerdict and print key and values
 

#### Question 4
# print all the keys , loop the innerdict and if a png filename is found, print key and values    
 
#q1
print ( "--- question 1 --- ")
print ( len(mydict) )
print ( mydict.keys() )
print ( mydict['window'].keys() )

# q3
print ( "--- question 4 --- ")
for key ,  innerdict in mydict.items(): 
    print ("\n", key, "---")
    for k , v in innerdict.items():
        print ( k, ":", v, end=";  ")
        
# q4
print ( "--- question 4 --- ")
print ( "---")
for key ,  innerdict in mydict.items(): 
    for k , v in innerdict.items():
        if type(v) == str :
            if 'png' in v:
                print (key,  k, "==>" , v)

# q4
print ( "--- question 4 --- ")
print ( "---")
for key ,  innerdict in mydict.items(): 
    for k , v in innerdict.items():
        try:
            if 'png' in v:
                print ("\n", key,  k, "==>" , v)
        except:
            print("",end ="")
        
