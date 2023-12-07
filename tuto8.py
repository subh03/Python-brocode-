#string slicing 
#slicing = create a substring by extracting elements from another string - indexing[] or slice() - [start:stop:step]

name = "subh megs"

first_name = name[0:4]
last_name = name[5:10]
funcky_name = name[0:10:2]
reversed_name = name[::-1]
#the starting index is inclusive and the stoping index is exclusive 

print(first_name)
print(last_name)
print(funcky_name)
print(reversed_name)



website1 = "https://www.google.com"
website2 = "https://www.wikipedia.com"

cutting_it = slice(12,-4)

print(website1[cutting_it])
print(website2[cutting_it])