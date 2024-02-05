cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if(car == 'bmw'):
        print(car.upper())
    else:
        print(car.title())

#Conditional test
#Checking for Eualities (run on terminal to see results)
car = 'audi'
car == 'bmw'
print(car)

#ignoring case when checking for euality(run on terminal to see results)

car = 'bmw'
car.upper() == 'Bmw'

#checking for ineualities
requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print("Hold the anchovies!")

#Checking whether element is not in list
banned_users = ['andrew', 'carolina', 'david', 'marie']
user = 'marie'

if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish")
else:
    print(f"{banned_users[0]}, you can go to hell")


#working with statements
age = 35
if age >= 50:
    print('You are an adult')
elif age == 35:
    print("you bi correct person")
else:
    print("you bi small pikin")

# checking for special items
requested_toppings = ['mushrooms', 'green pepper', 'cheese']
for requested_topping in requested_toppings:
    if requested_topping == 'green pepper':
        print("Sorry, we out of green pepper now")
    else:
        print(f"Putting {requested_topping}")
print("\nFinished cooking your pie")

del requested_toppings[0]
del requested_toppings[0]
del requested_toppings[0]
print(requested_toppings)
#checking for empty list
if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Putting {requested_topping}")
    print("\n Finished cooking pie")
else:
    print("You just cooked empty pie")



#using multiple list
available_toppings = ['mushrooms', 'olives', 'green peppers',
'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")
print("\nFinished making your pizza!")
