def printfirst(  ):  		#defining a function
   print ("Welcome to the Odeon Cinemas")
   
def getmoviename():  
    str = "The Wolf of Wall Street"
    return str

def printme( message ):
   print ("The movie showing today is " + message)

def printTickets(  movie, adults, c, p, ticketprice):
        print ( "Your movie choice:".ljust(20), movie)
        print ( "Ticket ordered: ")
        if adults > 0 : 
            print ( "Adults:".ljust(20), adults)
        if c > 0:
            print ( "Children:".ljust(20),c)
        if p > 0:
            print ( "Pensioners:".ljust(20),p) 
        print ( "Total Price:".ljust(20), ticketprice)
        
def giveNrPeople( msg ):  
    nr = float ( input (msg ) )
    return nr ;

def printme2 ( msg, value ) :
    print ( msg, value ) 

# what is the final goal / output
# what do I already know
# what are my problems, what must I calculate  calculations
# 1. get all input that will lead to the final goal, how many tickets, for c, a , p
# 2. create all calculations, using the input that will product the final goal, breaking it down in steps calulate the total
# 3. provide the final output print it
    
ticketprice = 10        
cprice = ticketprice / 2
pprice = ticketprice * 0.3
# problem
printfirst ()  	             # welcome		# gets nothing, returns nothing	 
moviename = getmoviename()   # welcome
printme (  moviename )       # welcome

# input
adults  = giveNrPeople ( "How many adult tickets? " ) 
children  = giveNrPeople ( "How many children tickets? " ) 
pensioners  = giveNrPeople ( "How many pensioner tickets? " ) 
# calculate
totalprice = ( adults * ticketprice ) + ( children * cprice ) + ( pensioners * pprice ) 

# Final output
#printme2 ( "Please pay", totalprice)
printTickets( moviename, adults, children, pensioners, totalprice)  # with details,  print







