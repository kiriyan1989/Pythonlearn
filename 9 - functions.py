##define the function using def keyword
## In Python the code inside the function need to be indented
# we pass the variable to function 
#just becasue a function is defined 
def say_hi(name, age):
    print("Hello  " + name + " you are " + str(age) + " old")
 #str(age) will convert anything to type string


##call the function , only when called the function is executed
print("Top") 

say_hi("Steve", 20) #string and Number
say_hi("Mike", "twenty-five") #string and string
say_hi("Kiriyan", True) #string and Boolen

print("Bottom")




##### Returns ######
#we can call a function and get a return back.
## we want it to execute the code and give code back
def cube(num):
    return num*num*num  # break out of function

print(cube(3))

result = 0 # the value of var result is 0
result = cube(4) # call the cube function with 4, the return will be stored here.
                #the new value of result var is the output of function cube.

print(result) # print the value of result var