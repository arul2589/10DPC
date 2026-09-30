################   File Handling  -- Test  ####################
'''
# Test 1

server = input("Enter server name: ")
status = input ("Enter status: ")

with open("server_status.txt","w") as file:
    file.write(f"Server: {server}\n")
    file.write(f"Status: {status}\n")

with open("server_status.txt","r") as file:
    content = file.read()

print (content)

'''
'''
# Test 2

env = "Production"

with open("server_status.txt","a") as file:
    file.write(f"Environment: {env}\n")

with open("server_status.txt","r") as file:
    content = file.read()

print (content)

'''
'''
# test 3

with open("server_status.txt","r") as file:
    contents = file.readlines()

for content in contents:
    content = content.strip()
    print (f"CONFIG: {content}")


'''

# test 4

userinput = input("Enter text to search: ")

with open ("server_status.txt","r") as file:
    content=file.read()

if userinput.lower() in content.lower():
    print (f"{userinput} found")
else:
    print (f"{userinput} not found")



# Test 5
'''
i=1


while i<=4:
    userinput = input(f"Enter Service {i}: ")
    i = i+1
    with open("aws_services.txt","a+") as file:
        file.write(f"{userinput}\n")

with open ("aws_services.txt","r") as file:
    contents = file.readlines()
    contents = set(contents)

print ("Unique AWS services:")
print("\n")
for content in contents:
    content = content.strip()
    
    print (content)
    
'''    

'''
i=1


with open("aws_services.txt","w") as file:
    while i<=4:
        userinput = input(f"Enter Service {i}: ")
        i = i+1
        file.write(f"{userinput}\n")

with open ("aws_services.txt","r") as file:
    contents = file.readlines()
    contents = set(contents)

print ("Unique AWS services:")
print("\n")
for content in contents:
    content = content.strip()
    
    print (content)
    

'''





