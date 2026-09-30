##################### Tuples & Sets ##################

######### 1 -- Tuple Basics


servers = ("EC2","S3","Lambda","RDS")

print (type(servers))
print (servers[0])
print (servers[-2])
print (servers[-1])


######### 2 -- Tuples Cannot Be Changed

#example 

services = ["EC2","S3","Lambda"]
services[1]="RDS"
print (services)

#AWS_services=("EC2","S3","Lambda")
#AWS_services[1] = "RDS"


#regions = ("ap-south-1", "us-east-1","eu-west-1")
#regions[1] = "us-west-1"
#print(regions)



######### 3 -- Loop Through a Tuple

services = ("EC2","S3","Lambda","RDS")

for service in services:
    print (f"Aws Service: {service}")




######### 4 -- Tuple Slicing


services = ("EC2","S3","Lambda","RDS","DynamoDB")

print(services[:3])
print(services[2:4])
print(services[-2:])



######### 5 -- Tuple Unpacking

server = ("web01", "Linux", "Tomcat")

name , os , application = server
print(name)
print (os)
print(application)

#name , os  = server

#print(name)
#print (os)


ec2 = ("tomcat01","t3.micro","ap-south-1")

name, instance_type, region = ec2

print(f"server {name} uses {instance_type} in {region}")


######### 6 -- Membership with in

#Example -1

regions = ("ap-south-1", "us-east-1", "eu-west-1")

if "ap-south-1" in regions:
    print("Region supported")
else:
    print("Region not supported")

#example-2
regions = ("ap-south-1", "us-east-1", "eu-west-1")

region = input("Enter AWS region: ")

if region in regions:
    print("Region supported")
else:
    print("Region not supported")



allowed_os = ("linux","windows","ubuntu")

user_os_request = input("Enter OS: ")

user_os_request = user_os_request.lower().strip()

if user_os_request in allowed_os:
    print("OS supported")
else:
    print("OS not supported")



######### 7 -- Sets

#Example-1

services = {"EC2", "S3", "Lambda", "RDS"}

print(services)
print(type(services))

#Example-2

services = {"EC2", "S3", "EC2", "RDS", "S3"}

print(services)



services = {"EC2", "S3", "EC2", "Lambda", "S3", "RDS"}

print (type(services))
print (services)
print(len(services))


#List  [] → ordered, duplicates allowed
#Tuple () → ordered, cannot be changed
#Set   {} → unique values, don't rely on order



######### 8 -- Add and Remove Set Items

services = {"EC2","S3","Lambda"}

services.add("RDS")
services.add("EC2")
services.remove("S3")
print(services)
print(len(services))



######### 9 -- Set Operations


devops = {"AWS","Linux","Docker","Terraform"}
genai = {"Python","AWS","LangChain","Linux"}

common = devops.intersection(genai)
all_tools= devops.union(genai)

print(common)
print(all_tools)