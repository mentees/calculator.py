#Input for numbers and operator
x = int(input("Please enter first_number-->: "))
operator = input ("please insert the operator -->: ")
y = int(input("Please enter second_number-->: "))

#Addition
if operator == "+":
    z = x + y
    print(f'You entered {x} + {y} youre answer is : {z}')

#Subtraction
elif operator == "-":
    z = x - y
    print(f'You entered {x} - {y} youre answer is : {z}')

#Multiplication
elif operator == "*":
    z = x * y
    print(f'You entered {x} * {y} youre answer is : {z}')

#Division with float
elif operator == "/":
    z = x / y
    print(f'You entered {x} / {y} youre answer is : {z}')

#Division
elif operator == "//":
    z = x // y
    print(f'You entered {x} // {y} youre answer is : {z}')
#Not supported operator
else :
    print("invalid input please try a valid operator(+,*,/,//,-)")