num = int(input("Enter Number : "))
for i in range(num):
    print("")
    for j in range(num):
        if j <= i:
            print("*", end="")
