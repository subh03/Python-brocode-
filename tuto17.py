#tuple = collection which is ordered and unchangeable 
#used to group together relate data 

student = ("subh",21,"male")

print(student.count("subh"))
print(student.index("male"))

for x in student:
    print(x)

if "subh" in student:
    print("subh is here!")
else:
    print("subh is not here!")
