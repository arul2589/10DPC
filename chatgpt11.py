###################### Strings & Text Processing #################################


###########    1 — String Indexing 

cloud = "Terraform"

print (cloud[0])
print (cloud[2])
print (cloud[-4])
print (cloud[-1])




###########    2 — String Slicing

technology = "Automation"

print (technology[0:4])
print (technology[4:])
print (technology[2:5])



###########    3 — upper() and lower()
env = input("Enter Environment: ")

if env.lower() == "production":
    print("Production environment selected")
else:
    print ("Other environment selected")


###########    4 — strip()

application = input("Enter Application: ")

if application.strip().lower() == "tomcat":
    print ("Tomcat application selected")

else:
    print("Other application selected")


###########    5 — replace()

request = "Create EC2 in us-east-1"

request = request.replace("us-east-1","ap-south-1")

print (request)


###########    6 — split()

request = "EC2,Linux,Tomcat,ap-south-1"

request = request.split(",")

print ("Service: ", request[0] )
print ("OS: ", request[1])
print ("Application: ",request[2])
print ("Region: ",request[3])


###########    7 — join()
server = ["web01","Linux","Tomcat","Production"]

result = " | ".join(server)

print (result)


###########    8 — startswith() and endswith()

filename = "production.tf"

if filename.endswith(".tf"):
    print ("Terraform file detected")
else:
    print ("Not a terraform file")




###########    9 — f-strings


server = "tomcat01"
instance_type = "t3.micro"
region = "ap-south-1"

print(f"Creating {server} with {instance_type} in {region}")