#for loop = a statement that will execute its block of code a limited amount of times 
# while loop = unlimited ; for loop = limited 

for i in range(10):
    print(i+1)

for i in range(50,100+1,3):
    print(i)

for i in "subh megs":
    print(i)

import time 
for seconds in range(10,0,-1):
    print(seconds)
    time.sleep(1)
print("Happy New Year! <3")