########################  Python Dictionaries ################################

server = {
    "name": "web01",
    "os": "Linux",
    "application": "Tomcat",
    "port": 8080
}

print(server["name"])
print(server["os"])
print(server["application"])
print(server["port"])

###Topic 1###
server = {
    "name" : "app01",
    "os" : "linux",
    "application" : "Tomcat",
    "port": 8080,
    "environment":"production"
}

print("Server name: " , server["name"])
print ("Operating System: ",server["os"])
print ("Application: ", server["application"])
print ("Port: ",server["port"])
print ("Environment: ",server["environment"])

###Topic 2###(Add and Update)
server = {
    "name" : "app01",
    "os" : "linux",
    "application" : "Tomcat",
    "port": 8080,
    "environment":"production"
}

server["instance_type"] = "t3.micro"

server["environment"] = "development"

print (server)

###Topic 3###(pop and del)
server = {
    "name" : "app01",
    "os" : "linux",
    "application" : "Tomcat",
    "port": 8080,
    "environment":"production"
}

server.pop("port")
del server["environment"]
print (server)

###Topic 4###(Keys and values)

aws = {
    "region": "ap-south-1",
    "instance": "t3.micro",
    "os": "Linux",
    "count": 2
}

print(aws.keys())
print(aws.values())


###Topic 5###(items())

print(aws.items())


aws = {
    "region": "ap-south-1",
    "instance": "t3.micro",
    "os": "Linux",
    "count": 2
}


for key , value in aws.items():
    print (key, " = ", value)



###Topic 6 ###( kays and values )

aws = {
    "region": "ap-south-1",
    "instance": "t3.micro",
    "os": "Linux",
    "count": 2
}



user_input = input("Enter Configuration name: ")

if user_input in aws:
    print("Configuration exists")

else:
    print("Configuration not found")



###Topic 7 ###( Nested )


aws_servers = {
    "web01" : {
        "os" : "Linux",
        "port" : 80
    },
    "db01" : {
        "os" : "Linux",
        "port": 3306
    }
}


print (aws_servers["web01"]["os"])
print (aws_servers["web01"]["port"])
print (aws_servers["db01"]["port"])
print(aws_servers["web01"])



###Topic 8 ###( Loop Through a Nested Dictionary )

aws_servers = {
    "web01" : {
        "os" : "Linux",
        "port" : 80
    },
    "db01" : {
        "os" : "Linux",
        "port": 3306
    }
}

for server, details in aws_servers.items():
    
    print("server: ",server)
    print("os: ",details['os'])
    print("port: ", details["port"] )



###Topic 9 ###( Dictionary with Lists )

aws = {
    "region": "ap-south-1",
    "services": ["EC2", "S3", "Lambda", "RDS"]
}

print ("Region: ", aws["region"])
for services in aws["services"]:
    print ("Service: ",services)