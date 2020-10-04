## all user inputs are string by default, we convert using float

num1 = float(input("Enter first numer"))   
op = input("Enter the operator")
num2 = float(input("Enter second numer"))

if op == "+":
    print (num1 + num2)
elif op == "-":
    print (num1 - num2)
elif op == "/":
    print (num1 / num2)
elif op == "*":
    print (num1 * num2)
else:
    print("Invalid operator")

