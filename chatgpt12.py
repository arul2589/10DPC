##################### Strings & Text Processing Test #######################
'''
############ Question 1

environment = input("Enter environment: ")

if environment.strip().lower()=="production":
    print("Production environment selected")
else:
    print("Non-production environment selected")


############ Question 2

request =  "Create EC2 in us-east-1"

request = request.replace("us-east-1","ap-south-1")

print (f"Updated Request: {request}")


############ Question 3

request = "EC2,Linux,Tomcat,ap-south-1"

request = request.split(",")
print(f"Service: {request[0]}")
print(f"OS: {request[1]}")
print(f"Application: {request[2]}")
print(f"Region: {request[3]}")


############ Question 4

services = ["EC2","S3","Lambda","RDS"]

services = " | ".join(services)

print(f"AWS Services: {services}")

'''
############ Question 5

filename = "   PRODUCTION.TF   "
filename = filename.strip().lower()

if filename.endswith(".tf"):
    print (f"Terraform file detected:{filename}")
else:
    print("Not a Terraform file")