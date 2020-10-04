def max_num(num1, num2, num3):      ## compare biggest number using if statements
    if num1 >= num2 and num1 >= num3:
        return num1                 #once we enter return the function is broken. 
      
    elif num2 >= num1 and num2 >= num3:
        return num2
    
    else:
        return num3

print(max_num(10, 10, 10.5))