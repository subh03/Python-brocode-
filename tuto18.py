#set = a collection which is unordered, unindexed. No duplicate values

subh = {"engineering","male",21,"student"}
megs = {"medical","female",20,"student"}

subh.add("handsome")
subh.remove("male")

love = subh.union(megs)

print(subh.intersection(megs))
print(subh.difference(megs))
print(subh.update(megs))

for x in love:
    print(x)