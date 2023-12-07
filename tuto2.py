#variables = a container for a value ; behaves as the value that it contains 
name = "subh"
print("hello "+name)
#print(type(name)) -> tell the class of variable
first_name = "subh"
last_name = "p"
full_name = first_name +" "+ last_name 
print("Hello "+full_name)

age = 21
#int data type - we dont use ""
age = age+1 
#can be written as age += 1
print(age)
print(type(age))
print("your age is : "+str(age))
#using string cast to convert int to string before using it with string (typecasting)

#float = floating point number (a decimal number)
height = 180.3 
print(height)
print(type(height))
print("your height is :"+str(height)+" cm")

#boolean data type = a variable which can only store true or false (very useful for if statements)
human = True 
print(human)
print(type(human))
print("are you a human : "+str(human))
