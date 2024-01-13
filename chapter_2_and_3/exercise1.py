names = ['KElly', 'Butlar', 'Desmond', 'Wes']
print(names[0])
print(names[1])
print(names[2])
print(names[3])

message = f"hello {names[0]}."
print(message)

# Exercise 2
guests = ['Noel', 'Ken', 'Wes', 'Shen', 'Bes']
print(f"You are invited {guests[0]}")
print(f"You are invited {guests[1]}")
print(f"You are invited {guests[2]}")
print(f"You are invited {guests[3]}")
print(f"You are invited {guests[4]}")
absent_guest = guests.pop(2)
print(f"{absent_guest} can't make it ")
guests.append('Mary')
print(f"You are invited {guests[0]}")
print(f"You are invited {guests[1]}")
print(f"You are invited {guests[2]}")
print(f"You are invited {guests[3]}")
print(f"You are invited {guests[4]}")
guests.insert(0, 'John')
guests.insert(3, 'Pel')
guests.append('Jack')
print(f"You are invited {guests[0]}")
print(f"You are invited {guests[1]}")
print(f"You are invited {guests[2]}")
print(f"You are invited {guests[3]}")
print(f"You are invited {guests[4]}")
print(f"You are invited {guests[5]}")
print(f"You are invited {guests[6]}")
print(f"You are invited {guests[7]}")

print("\n Sorry guys, I can only invite 2 persons")
removed_guest1 = guests.pop()
print(f"{removed_guest1} Sorry!")
removed_guest2 = guests.pop()
print(f"{removed_guest2} Sorry!")
removed_guest3 = guests.pop()
print(f"{removed_guest3} Sorry!")
removed_guest4 = guests.pop()
print(f"{removed_guest4} Sorry!")
removed_guest5 = guests.pop()
print(f"{removed_guest5} Sorry!")
removed_guest5 = guests.pop()
print(f"{removed_guest5} Sorry!")
print(guests)

print(f"You are invited {guests[0]}")
print(f"You are invited {guests[1]}")

del guests[1]
del guests[0]
print(guests)