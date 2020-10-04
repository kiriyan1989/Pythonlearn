#### python file read commands ####


######   Get the current working direcory: os.getcwd()   ######   
import os
cwd = os.getcwd()
print("current dir is " + cwd)       # show current working dir

##########   Get the path of running file (.py) in Python: __file__ ###########
print(" the python file being exeucted __file__ is : ", __file__)        
# ^^^ shows current py file being executed.

## read 'r' or 'w' mode or 'a' append, 'r+' read and write
hello = open("/Users/kiriyan/VS Code/1/hello.txt", "r") # absoloute path to file, read mode
if hello.readable() == True:    # if we can read the file 
    for names in hello.readlines():
        print(names)



print(hello.readline())     # read file line 1

print(hello.readlines()[1]) # read items in the file and put in array

hello.close()



"""
path = os.getcwd()
print("the dir is:")
print(path)
print(type(path))

open("/Users/kiriyan/hello.txt", 'r')
"""

"""
with open("hello.txt", "r") as f:
    print(f)

import os
with open(os.path.join(sys.path[0], "hello.txt"), "r") as f:
    print(f.read())

if employee_file.readable() == True:
    print(employee_file)
else:
     print("cant read file")

# after we opne the file, we should close the file.
employee_file.close()
"""