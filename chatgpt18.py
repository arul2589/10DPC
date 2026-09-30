########################## Exception Handling -- Test #######################


'''
try:
    server_port = int(input("Enter Server port: "))

    if server_port <1 or server_port >65535:
        raise ValueError("Port must be between 1 and 65535")

except ValueError as error:
    print (f"Error: {error}")

else:
    print (f"Valid port: {server_port}")

'''
'''
try:
    filename = input("Enter filename: ")

    with open(filename , "r") as file:
        content = file.read()
    if "production" in content.lower():
        result =("Production environment found")
    else:
        result =("Production environment not found")

except FileNotFoundError:
    print ("File not found")

else:
    print(result)
'''
'''
try:
    instance_count = int(input("Enter instance count: "))
    price_per_instance = int(input("Enter price per instance: "))
    if instance_count < 1:
        raise ValueError ("instance count must be al least 1")
    
    total_cost = instance_count * price_per_instance

except ValueError as error:
    print (f"Error: {error}")

else:

    print(f"Total cost: {total_cost}")

'''
'''
def calculate_division(num1, num2):
    return (num1/num2)

try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = calculate_division(num1,num2)
    
except ZeroDivisionError:
    print ("Cannot divide by zero")

except ValueError:
    print ("Please enter numbers only")

else:
    print(f"Result: {result}")
'''
try:

    server_name = input("Enter server name: ")
    instance_count = int(input("Enter instance count:"))
    server_port = int(input("Enter server port: "))

    if instance_count <1:
        raise ValueError("Instance count must be at least 1")

    elif server_port <1 or server_port > 65535:
        raise ValueError("Port must be between 1 and 65535")

    with open("aws_request.txt","w") as file:
        file.write (f"Server: {server_name}\n")
        file.write (f"Instance: {instance_count}\n")
        file.write (f"Port: {server_port}\n")

except ValueError as error:
    print (f"Error: {error}")

else:
    print("AWS request created successfully")

finally:
    print("Request processing completed")
