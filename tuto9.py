#if statement = a block of code that will execute if its condition is true

age = int(input("How old are you? : "))

#the order of the if statements does matter

if age == 100:
    print("Great, you scored a century!")
elif age >= 18:
    print("You are an adult!")
elif age < 0:
    print("You haven't been born yet!")
else: 
    print("You are a child!")