def greet(first_name, last_name):
    print(f"Hello, {first_name} {last_name} \nWelcome OnBoard 😎 😎  🎈🎈")
    return


firstName = input("First Name : ")
lastName = input("Last Name : ")
greet(firstName, lastName)

# reverse array itteration.

for i in range(10, 0, -1):
    print(i, end=" ")
