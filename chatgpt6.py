################ Chat GPT test on LIST#################


skills = ["AWS", "Linux", "Docker"]

skills.append("Terraform")
skills.insert(0,"Python")
skills.pop(-3)
print (skills)
print(len(skills))



skills = ["Python", "AWS", "Java", "Linux", "Terraform", "Docker"]

for skill in skills:
    if skill == "Java":
        continue
    print(skill)



allowed_servers = ["web01", "web02", "app01", "db01"]

server_name = input("Enter Server name : ")

if server_name in allowed_servers:
    print("Server is availabe")

else:
    print("server not availabe")


servers = ["web01", "web02", "app01", "app02", "db01", "db02"]

print (servers[2:5])

print (servers[4:])



servers = ["web01", "app01", "db01"]

new_server = input("Enter New Server name : ")

if new_server in servers:
    print("Server already exist")
    print(servers)
else:
    servers.append(new_server)
    print (servers)
    print("Server added successfully")