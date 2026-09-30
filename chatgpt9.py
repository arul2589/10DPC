
######################  Python Functions  ###############################
############ topic 1   What is a Function?  

def aws_info():
    print("Welcome to AWS Automation")
    print("Learning pyton Functions")

aws_info()
aws_info()


############ topic 2   Function Parameters


def aws_server(server):
    print ("Checking server: ", server)

aws_server("web01")
aws_server("tomcat01")
aws_server("db01")


############ topic 3   Multiple Parameters

def create_ec2(name,instance_type,region):
    print ("Server: ",name)
    print ("Instance Type: ", instance_type)
    print ("Region: ", region)

create_ec2("tomcat01","t3.micro","ap-south-1")
create_ec2("db01","t3.small","us-east-1")


############ topic 4   return

def calculate_cost(instance_cost, hours):
    return instance_cost*hours

total = calculate_cost(5, 10)
print ("total Cost: ",total)


############ topic 5   if/else Inside a Function

def check_port(port):
    if port == 80:
        return "HTTP"
    elif port == 443:
        return "HTTPS"
    else:
        return "Unknown Port"

print (check_port(80))
print (check_port(443))
print (check_port(8080))



############ topic 6   Loop Inside a Function

services = ["EC2","S3","Lambda","RDS"]


def show_services(services):
    for service in services:
        print ("AWS Service: ", service)

show_services(services)



############ topic 7   Passing a Dictionary to a Function

ec2 = {
    "name":"web01",
    "instance_type": "t3.micro",
    "region":"ap-south-1",
    "status":"running"
}

def ec2_info(ec2):
    print ("EC2 Name: ", ec2["name"])
    print ("Instance Type: ", ec2["instance_type"])
    print ("Region: ", ec2["region"])
    print ("Status: ",ec2["status"])

ec2_info(ec2)



############ topic 8   Default Parameter

def create_ec2(name, instance_type = "t3.micro"):
    print("Server: ",name)
    print("Instance Type: ",instance_type)

create_ec2("web01")
create_ec2("db01","t3.large")



############ topic 9   Keyword Arguments

def deploy_server(name,os,region):
    print("Name: ",name)
    print("OS: ",os)
    print ("Region: ",region)


deploy_server(
    region="us-east-1",
    name="tomcat01",
    os="Linux"
)

