################# Tuple & Set Test #########
'''
# Question 1
server = ("tomcat01", "Linux", "Tomcat", "ap-south-1")

name, os, application, region = server

print(f"Server {name} runs {application} on {os} in {region}")



# Question 2

allowed_regions = ("ap-south-1", "us-east-1","eu-west-1")

user_region_info = input("Enter AWS region: ")
user_region_info = user_region_info.strip()

if user_region_info in allowed_regions:
    print ("Region supported")
else:
    print ("Region not supported")



# Question 3

services = ["EC2", "S3", "EC2", "Lambda", "S3", "RDS", "EC2"]

uni_services= set(services)

print(uni_services)
print(len(uni_services))

# Question 4

devops = {"AWS", "Linux", "Docker", "Terraform"}
cloud = {"AWS", "Linux", "Kubernetes", "Python"}

common = devops.intersection(cloud)

all_skills = devops.union(cloud)

print (f"Common: {common}")
print (f"All Skills: {all_skills}")

'''
# Question 5

allowed_services = ("ec2", "s3", "lambda", "rds")


user_services_info = input("Enter services separated by comma:")
user_services_info = user_services_info.lower()

user_services_info = user_services_info.split(",")

user_services_info= set(user_services_info)


for user_request in user_services_info:
    if user_request in allowed_services:
        print (f"{user_request} is allowed")
    else:
        print (f"{user_request} is not allowed")
    
