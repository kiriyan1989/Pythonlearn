
try:        ## allows us to try
    value = 10 /0
    number = float(input("Enter a number "))
    print(number)

## catch erros using the below combined with try above ##

#except:             
             # catch all errors - very broad, not useful.

## we can catch different kind of errors ##
except ZeroDivisionError as err:             
    print("divided by 0")
    print(err)

except ValueError:
     print("invalid input")
