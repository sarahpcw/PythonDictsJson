#1. Create a class
#2. indent everything in the class
#3. use the keyword self , must be the first parameter in all the functions

class movieFunctions:
    
    def print_this(movies):
         for col in range (0,len(movies[0]),1):
             for j in range ( 0 , len(movies), 1):
                 print ( movies[j][col].ljust(10) , end = "  " ) 
             print (' ')
        
        
    def askTicketNumbers (  self ):
        a = int( input ( "How many adults want to buy a movie ticket? "))
        p = int( input ( "How many pensioners want to buy a movie ticket? "))
        c = int( input ( "How many Children want to buy a movie ticket? "))
        return a,p,c

    def printTickets( self , movie, adults, c, p, ticketprice):
        print ( "Your movie choice:".ljust(20), movie)
        print ( "Ticket ordered: ")
        if adults > 0 : 
            print ( "Adults:".ljust(20), adults)
        if c > 0:
            print ( "Children:".ljust(20),c)
        if p > 0:
            print ( "Pensioners:".ljust(20),p) 
        print ( "Total Price:".ljust(20), ticketprice)

