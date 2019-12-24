def factorial(num):
    if num <= 2 and num > -1:
        return num
    return num * factorial(num-1)


num = int(input("Enter Number : "))
print(factorial(num))
