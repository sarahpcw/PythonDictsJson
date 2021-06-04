##########################################################3
##create a json file as output by dumping a dictionary to a json file
import json
people = {'emp1': {'name': 'John',  'age': '27', 'gender': 'Male'},
          'emp2': {'name': 'Marie', 'age': '22', 'gender': 'Female'} ,
          'emp3': {'name': 'Peter', 'age': '29', 'gender': 'Male', 'married': 'Yes'},
          'emp4': {'name': 'Paul',  'age': '31', 'gender': 'Male', 'married': 'No'}}


with open('C:\\Users\\u\\.spyder-py3\\3W-Webinar\\myfileApril.json', 'w') as peopleFile: 
    json.dump(people, peopleFile)    # put people dictionary into people file as json format
#
##open  a json file and put it into a dictionary
with open('C:\\Users\\u\\.spyder-py3\\3W-Webinar\\student_score.json', 'r') as peopleFile:
  newpeople = json.load(peopleFile) 		# use s i.e. loads when creating the dictionary from a FILE

print(len(newpeople))

sumS = 0
sumM = 0
sumE = 0
sumL = 0
classList = []
classCounts = []
print ('--- Student Averages ---')
for key,val in newpeople.items():
    studentavg =  (val['math'] +val['science'] + val['english'] + val['literature'])/4
    print (key, "=>", studentavg)
    sumS += val['science']
    sumM += val['math']
    sumE += val['english']
    sumL += val['literature']
    if val['class'] not in classList :  
        classList.append(val['class'])     # classList : ['10-a']
        classCounts.append(0)
    if val['class'] in classList  :
        i = classList.index(val['class'])  # counting how many people per class
        classCounts[i] += 1

print ('--- Class Counts ---')
for i in range ( len(classList )) :
    print ( classList[i], classCounts[i])
    
print ('--- Subject Averages ---')
print('avgS', sumS/len(people))
print('avgM', sumM/len(people))
print('avgE', sumE/len(people))
print('avgL', sumL/len(people))

#]]=\
    
#C:\Users\u\Downloads\archive (1)

with open('C:\\Users\\u\\Downloads\\archive (1)\\marketing_sample_for_careerbuilder.json', 'r', encoding="UTF-8") as peopleFile:
  newpeople = json.load(peopleFile) 