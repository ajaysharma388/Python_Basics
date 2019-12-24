while True:
    command = input(f"@{username} >>> ")
    print(f"echo, {command}")
    if command.lower() == "quit":
        break

command = ""

while command.lower() != "quit":
    command = input(">>> ")
    print(f"echo, {command}")


username = input("Enter Your Username : ")
password = input("Password : ")
