start = int(input("Enter Start Value : "))
end = int(input("Enter end Value : "))
start = start if start >= 2 else 3
# inc = 1 if start%2 ==0 and start!=2 else 2
for i in range(start, end, 1):
    j = 2
    while j*j <= i:
        if i % j == 0:
            break
        j += 1
    else:
        print(i, end=" ")
# Sample Input :

# Enter Start Value : 1
# Enter end Value : 100

# Sample Output :

# 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97
