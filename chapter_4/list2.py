#Slicing a lihst
list = ['cool', 'bed', 'shoe', 'leg', 'hon']
print(list[0:3])
print(list[:2])
print(list[2:])
for l in list[2:3]:
    print(l.title())

#copying list
list_copy = list[:]
print(list_copy)