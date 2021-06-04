import json 
j_i = {
  "colors": [
    {
      "color": "black",
      "category": "hue",
      "type": "primary",
      "code": {
        "rgba": [255,255,255,1],
        "hex": "#000"
      }
    },
    {
      "color": "white",
      "category": "value",
      "code": {
        "rgba": [0,0,0,1],
        "hex": "#FFF"
      }
    },
    {
      "color": "red",
      "category": "hue",
      "type": "primary",
      "code": {
        "rgba": [255,0,0,1],
        "hex": "#FF0"
      }
    },
    {
      "color": "blue",
      "category": "hue",
      "type": "primary",
      "code": {
        "rgba": [0,0,255,1],
        "hex": "#00F"
      }
    },
    {
      "color": "yellow",
      "category": "hue",
      "type": "primary",
      "code": {
        "rgba": [255,255,0,1],
        "hex": "#FF0"
      }
    },
    {
      "color": "green",
      "category": "hue",
      "type": "secondary",
      "code": {
        "rgba": [0,255,0,1],
        "hex": "#0F0"
      }
    },
  ]
}

print ( j_i['colors']['color'])
for y,x in j_i.items():
    print (y, "=>", type( x ) )
    for i in range (len(x) ) :
        print ( '----------')
#        print (x[i], type(x[i]))
        if type(x[i]) == dict:
            for k,v in x[i].items():
                print (k,'===>',v)

##Jason example 3
#with open('JsonMoviesInputXy.txt', 'w') as outfile:
#    json.dump(j_i, outfile)
#with open('JsonMoviesInputX.json', 'w') as outfile:
#    json.dump(j_i, outfile)  
#
#
#with open('JsonMoviesInputX.json') as json_data:
#    d = json.load(json_data)
#    print(d)
#    for key,val in d.items():
#        print (key, "=>", val)
