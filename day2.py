numbers = {10, 20, 30}
num = {10, 20, 10}

print(num)
print(numbers)  # Contains only 10 and 20; order may vary

numbers.add(30)
numbers.remove(10)
numbers.add(50)

print (numbers)