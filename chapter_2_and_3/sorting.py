#permenent sorting with  the sort()  method
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars) #arranges it alphabetically

# this could be done in reverse order
cars.sort(reverse=True)
print(cars)
#sorting

# to maintain the original list even after sorting
print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the original list again:")
print(cars)
 #printinng a list in reverse order
cars.reverse()
print(cars)


#legth of a list
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars))
