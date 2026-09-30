###############     Functions test    #######################

##### Question 1

def calculate_storage_cost(size, price):
    return size*price

cost = calculate_storage_cost(100, 2)

print("Storage Cost: ",cost)



##### Question 2

def check_instance(instance_type):
    if instance_type == "t3.micro":
        return ("Development Server")
    elif instance_type == "t3.small":
        return ("Testing Server")
    elif instance_type == "m5.large":
        return ("Production Server")
    else:
        return("Server details not found")


print (check_instance("t3.micro"))
print (check_instance("t3.small"))
print (check_instance("m5.large"))
print (check_instance("t2.small"))


##### Question 3

servers = ["web01","app01","db01","test01"]

def show_servers(servers):
    for server in servers:
        if server == "test01":
            continue
        print ("Server: ",server)

show_servers(servers)



##### Question 4


server = {
    "name":"tomcat01",
    "os":"Linux",
    "status":"running"
}

def check_server(server):
    if server["status"]=="running":
        return server["name"]+" is available"
    else:
        return  server["name"]+" is not available"

result =check_server(server)
print (result)



##### Question 5


servers = {
    "web01":"running",
    "app01":"stopped",
    "db01":"running"
}

def count_running(servers):
    count =0
    for value in servers.values():
        if value == "running":
            count= count + 1
    return count

        
total = count_running(servers)
print ("Running Servers: ", total)