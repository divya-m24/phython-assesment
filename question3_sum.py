n = int(input("Enter a positive number: "))

total = 0

for i in range(1, n + 1):
    total = total + i

print("Sum of numbers from 1 to", n, "is:", total)