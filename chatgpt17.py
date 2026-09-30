########################## Exception Handling #######################

########### 1 --  try and except
'''
try:
    age = int(input("Enter Your age: "))

    print (f"Your age is {age}")
except:
    print ("Inavlid age")



########### 2 --  Catching a Specific Error

#exercise

try:

    first_num = int(input("Enter first number: "))
    second_num = int(input("Enter second number: "))
    add = first_num + second_num
    print (f"Total: {add}")

except ValueError:

    print("Please enter numbers only")



########### 3 --  Multiple Exception Types

#exercise

try:
    
    number1 = int(input("Enter first number: "))
    number2 = int(input("Enter second number: "))
    result = number1/number2
    print (f"Result: {result}")
except ValueError:
    print ("Please enter numbers only")
except ZeroDivisionError:
    print ("Cannot divide by zero")



########### 4 --  else

#exercise

try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter Second number: "))
    result = num1/num2

except ValueError:
    print ("Please enter numbers only")

except ZeroDivisionError:
    print ("Cannot divide by zero")

else:
    print(f"Division successful\nResult: {result}")



########### 5 --  finally

#exercise


try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter Second number: "))
    result = num1/num2

except ValueError:
    print ("Please enter numbers only")

except ZeroDivisionError:
    print ("Cannot divide by zero")

else:
    print(f"Division successful\nResult: {result}")

finally:
    print("Calculation Completed")


########### 6 --  FileNotFoundError

#exercise

try:
    filename = input("Enter filename: ")
    with open(filename,"r") as file:
        content = file.read()
except FileNotFoundError:
    print ("File not found")
else:
    print(f"File opened successfully\n{content}")



########### 7 --  Getting the Actual Error Message

#exercise

try:
    age = int(input("Enter age: "))

except ValueError as error:
    print("Invalid input")
    print(error)
else:
    print(f"Age: {age}")



########### 8 --  Catching Any Exception with Exception

#exercise

try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter Second number: "))
    result = num1/num2

except Exception as error:
    print(f"Something went wrong\n{error}")

else:
    print(f"Result: {result}")

'''
########### 9 --  Catching Any Exception with Exception

#exercise

try:
    instance_count = int (input("Enter instance count: "))
    if instance_count < 1:
        raise ValueError("Instance count must be at least 1")

except ValueError as error:
    print (f"Error: {error}")

else:
    print (f"Instance count: {instance_count}")