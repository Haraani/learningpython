# Program to learn arthematic operations 

# This function performs addition of two numbers
def add(x, y):
    return x + y
# This function performs subtraction of two numbers
def subtract(x, y):
    return x - y

# This function performs multiplication of two numbers
def multiply(x, y):
    return x * y

# This function performs division of two numbers
def divide(x, y):
    return x / y
#this function gives the modulus
def modulus(x, y):
    return x%y

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5. Modulus")
while True:
    # Take input from the user
    select = input("Enter choice(1, 2, 3, 4 or 5): ")

    # Check if choice is one of the four options
    if select in ('1', '2', '3', '4', '5'):
        number1 = float(input("Enter first number: "))
        number2 = float(input("Enter second number: "))

        if select =='1':
            print("You have selected Addition:\n")
            print(" The Sum of {} and {} is {}".format(number1, number2, addition(number1,number2)))
        elif select == '2':
            print("You have selected Subtraction:\n")
            print(" The Difference between {} and {} is {}".format(number1, number2, subtract(number1, number2)))
        elif select == '3':
            print("You have selected Multiply:\n")
            print(" The product of {} and {} is {}".format(number1, number2, multiply(number1, number2)))
        elif select == '4':
            print("You have selected Division:\n")
            print(" The result when {} is divided by {} is {}".format(number1, number2, divide(number1, number2)))
        elif select == '5':
            print("You have selected Modulus:\n")
            print(" The modulus of {} and {} is {}".format(number1, number2, modulus(number1, number2)))      
        break
    else:
        print("Invalid Input")
