#logical operators (and,or,not) = used to check if two or more conditional statements is true 

temp = int(input("What is the temperature outside?"))

if temp >= 0 and temp <= 30:
    print("The temperature outside is good!")
    print("Go out and have a nice day :)")

elif temp < 0 or temp > 30: 
    print("THe temperature is bad today!")
    print("Try to stay inside")

if not(temp >= 0 and temp <= 30):
    print("The temperature outside is good!")
    print("Go out and have a nice day :)")

#not reverses the roles of the conditions - true -> false ; false -> true 