start = 2
end = int(input("Enter End : "))
count = 0
while start <= end:
    print(start, end=" ")
    start += 2
    count += 1
print(f"\nWe have {count} Even numbers from 0 to {end}.")
count = 0
for i in range(0,end,2):
    if i>0 and i%2==0:
        print(i,end=" ")
        count += 1    
print(f"\nWe have {count} Even numbers from 0 to {end}.")