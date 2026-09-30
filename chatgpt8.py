################ Chat GPT test on Dictionary#################


############ Question 1 #####################
ec2 = {
    "name": "tomcat01",
    "instance_type": "t3.micro",
    "region": "ap-south-1"
}

ec2["os"] = "Linux"

ec2["instance_type"] = "t3.small"

del ec2["region"]

print(ec2)

############ Question 2 #####################

ec2 = {
    "name": "tomcat01",
    "instance_type": "t3.small",
    "os": "Linux",
    "port": 8080
}

user_input = input("Enter Configuration: ")

if user_input in ec2:
    print(ec2[user_input])
else:
    print("Configuration not found")

############ Question 3 #####################

servers = {
    "web01": {
        "os": "Linux",
        "port": 80
    },
    "tomcat01": {
        "os": "Linux",
        "port": 8080
    },
    "db01": {
        "os": "Linux",
        "port": 3306
    }
}

for server , details in servers.items():
    print(server, "runs on port ",details["port"])

############ Question 4 #####################

aws = {
    "region": "ap-south-1",
    "services": ["EC2", "S3", "Lambda", "RDS", "DynamoDB"]
}

for details in aws["services"]:
    if details == "Lambda":
        continue
    print (details)


############ Question 5 #####################

servers = {
    "web01": {
        "os": "Linux",
        "status": "running"
    },
    "app01": {
        "os": "Linux",
        "status": "stopped"
    },
    "db01": {
        "os": "Linux",
        "status": "running"
    }
}

for server, details in servers.items():

    if details["status"] == "stopped":
        continue

    print (server, " is ",details["status"])