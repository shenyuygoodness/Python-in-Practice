users = ['admin', 'Tie', 'peter', 'John', 'Cle']
#Hello admin
for user in users:
    if user != '':
        if user == 'admin':
            print(f"Hello {user.title()}, would you like to see a status report?")
        else:
            print(f"Hello {user.title()}, thank you for logging in again.")
    else:
        print("We need to find some users")
# checks for No users done up

#checking usernames
current_users = users
new_users =['Cle', 'Bel', 'Tie', 'shen']
for current_user in current_users:
    for new_user in new_users:
        if current_user == new_user:
            print("Please input a new username")
        else:
            print("Username available")

