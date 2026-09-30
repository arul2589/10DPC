################ File Handling ####################

########### 1 --- Creating and Writing a File "w"

#example

file = open("server.txt", "w")

file.write("Ngenix")

file.close()

# exercise #

file = open("aws_server.txt","w")

file.write("web01")

file.close()



########### 2 --- Writing Multiple Lines "/n"

# Example -1
file = open("server_info.txt", "w")

file.write("Server: web01\n")
file.write("OS: Linux\n")
file.write("Application: Tomcat\n")

file.close()


# exercise #

file = open("aws_info.txt","w")
file.write("Server: tomcat01\n")
file.write("OS: Linux\n")
file.write("Instance: t3.micro\n")
file.write("Region: ap-south-1")


########### 3 --- Reading a File "r"

# exercise #

file = open("aws_info.txt","r")
content = file.read()
print(content)
file.close()


########### 4 --- Append Mode "a"
# exercise #
file = open("aws_info.txt","a")
file.write("\nApplication: Tomcat\n")
file.write("Status: Running")
file.close()

file = open("aws_info.txt","r")
content = file.read()
print (content)


########### 5 --- with open()
# exercise #

with open("aws_info.txt","r") as file:
    content = file.read()
print(content)


########### 6 --- readlines()
# exercise #

with open("aws_info.txt","r") as file:
    contents=file.readlines()

for content in contents:
    content = content.strip()
    print (f"INFO: {content}")


########### 7 --- Writing Variables to a File
# exercise #


server = input("Enter Server name: ")
os = input("Enter OS: ")
application = input("Enter Application: ")
region = input ("Enter region: ")

with open("server_config.txt","w") as file:
    file.write(f"Server: {server}\n")
    file.write(f"OS: {os}\n")
    file.write(f"Application: {application}\n")
    file.write(f"Region: {region}\n")

with open("server_config.txt","r") as file:
    content = file.read()
print (content)


########### 8 --- Check Whether Text Exists in a File
# exercise #


application = input("Enter application to search: ")

application = application.lower()
application = application[0].upper()+application[1:]
print (application)

with open("server_config.txt","r") as file:
    content = file.read()

if application in content:
    print (f"{application} found in configuration")
else:
    print (f"{application} not found in configuration")


########### 9 --- readline()
# exercise #

with open("server_config.txt","r") as file:
    line1 = file.readline()
    line2 = file.readline()
    line3 = file.readline()
    line4 = file.readline()

print (line1.strip())
print (line3.strip())