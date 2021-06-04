#firstname = input("Please enter your name")
# carpet quotes 



print ( "Welcome to ABC Carpets!" )


width  = input("What is the width?")
length = input("What is the length?")
#width = int(width)
#length = int(length)

width = float(width)
length = float(length)

print ("Width", width)
print ( "Length ", length )



area = width * length  # + - * / ()
print ( "Area", area )
#


sqm_price = 15
carpetprice = area * sqm_price * 1.2
print ( "Carpet price ", "%.2f" % carpetprice)


