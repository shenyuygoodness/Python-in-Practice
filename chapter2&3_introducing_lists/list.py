bikes = ['host', 'redline', 'trek', 'bread']
print(bikes)

#Accessing elements in a list
print(bikes[0])  # this is done by use of indexes

# for more modification
print(bikes[2].title())

# acessing last elements in the list
print(bikes[-1])
# using individual values from a list
message = f"My first bike was a {bikes[3].title()}."
print(message)

#Modifying elements in a list
# changing elements in a list

motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles[0] = 'ducati'
print(motorcycles)

# Adding an element to the list using append
motorcycles.append('ducati')
print(motorcycles)
 
#Inserting elements into a list
motorcycles.insert(2, 'benz')
print(motorcycles)

#Removing elements from a list
#1) using del statement
del motorcycles[1]
print(motorcycles)
#2) using pop() method
popped_motocycle = motorcycles.pop()
popped_motocycles = motorcycles.pop(0)
print(motorcycles)
print(popped_motocycle)

# 3) removing by value using remove method
motorcycles.remove('suzuki')
print(motorcycles)