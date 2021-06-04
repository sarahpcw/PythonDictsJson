def mult (x ):
    x = x * 2
    return x 

calc_times2 = lambda x : x * 2 



x =  calc_times2 ( 23 )
print ( x )

print ( ' 23' , calc_times2 ( 23 ) )

print ( ' 33' , calc_times2 ( 33 ) )

print ( ' 51' , calc_times2 ( 51 ) )

print ( ' 10' , calc_times2 ( 10 ) )
#






calc_Addition = lambda x,y : x + y 
print ( ' 2 plus 3 :' , calc_Addition( 2,3 ))
print ( ' 3 plus 3 :' , calc_Addition( 3,3 ))
print ( ' 5 plus 1 :' , calc_Addition( 5,1 ))
print ( ' 1 plus 0 :' , calc_Addition( 1,0 ))



fahr = lambda x : ( x * 9 /5 ) + 32
print ( 'fahr' , fahr( 0 ))





calcMovieTicket = lambda pr, a, c, p : pr*a +(pr*c/2) + (pr*p*0.3)

print ( "TotalPrice" , calcMovieTicket(10,2,0,0))






Celcius = [27.2 ,24.2 ,26.7 ,38.5]
for i in range ( 0 , len(Celcius), 1):
    f = ( Celcius[i] * 9 /5 ) + 32
    print (f)
  

Fahrenheit = map ( lambda x : (x  *  9/5 ) + 32   , Celcius ) 
print (Fahrenheit) # Fahrenheit is not a list 
for each in Fahrenheit: 
    print (each)
    
# if I want to also access Celcius using corresponding indexes
Fahrenheit =  list (  map  ( lambda x : (x  *  9/5 ) + 32   ,  Celcius ) )
i = 0
print (Fahrenheit)
for i  in range (len(Fahrenheit))  :
    print ('Fahrenheit vs Celcius ' , Fahrenheit[i], ' ' , Celcius[i] ) 
  


