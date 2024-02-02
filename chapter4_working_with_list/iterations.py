magicians = ['alice', 'david', 'caro']
for magician in magicians:
    print(magician) 
    print(f"{magician.title()}, that was a great trick\n")

#printing ranges 
for value in range(2, 6):
    print(value)

#printing lists
numbers = list(range(2, 7))
print(numbers)

#getting list of numbers based on the adding a particular number
even_numbers = list(range(2, 56, 5))
print(even_numbers)

rectangles = []
for v in range(2, 23):
    rectangle = v ** 2
    rectangles.append(rectangle)
    print(rectangles)

# the above could be done in 2 lines
rectangle = [value**2 for value in range(2, 22)]
print(rectangle)

#using methods

print(max(rectangles))
print(max(numbers))
print(sum(even_numbers))