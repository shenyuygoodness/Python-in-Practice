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
#Turples
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
#dimensions[0] = 45 this will produce errors when printed, showing it won't be possible to modify turples 
for dimension in dimensions:
    print(dimension)
# tuples can be modified like variables
dimensions = (56, 67)
print(dimensions)
