################### List Practice ################################ 


technologies=["python","AWS","Linux","terraform","GenAI"]

print(technologies[0])
print(technologies[2])
print(technologies[4])


print(technologies[-1])
print(technologies[-3])
print(technologies[-5])




technologies = ["python","AWS","Linux"]

technologies[2] = "Terraform"
technologies.append("GenAI")

print (technologies)



tools = ["python","AWS","Terraform","GenAI"]

tools.insert(2, "Docker")
print(tools)



tools = ["Python", "AWS", "Linux", "Docker", "Terraform", "GenAI"]

tools.remove("Linux")
print (tools)
tools.pop(2)
print (tools)


tools = ["Python", "AWS", "Linux", "Docker", "Terraform", "GenAI"]
print(len(tools))



tools = ["Python", "AWS", "Linux", "Docker", "Terraform", "GenAI"]

for tool in tools:
    print(tool)



cloud = ["AWS", "Azure", "GCP", "Oracle"]

for learning in cloud:
    print("I am learning", learning)


skills = ["Python", "AWS", "Linux", "Terraform", "Docker"]

skill = input("Enter your Skill :")

if skill in skills:
    print(skill,"Is available")

else:
    print(skill,"Is not available")

tools = ["Python", "AWS", "Linux", "Docker", "Terraform", "GenAI"]

print(tools[1:4])
print(tools[3:])



marks = [75, 40, 95, 60, 85, 50]

marks.sort()
print (marks)

marks.reverse()
print (marks)