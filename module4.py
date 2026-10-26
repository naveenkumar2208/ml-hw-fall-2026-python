n = int(input("Enter N: "))
numbers = []
for i in range(n):
    numbers.append(int(input(f"Enter number {i + 1}: ")))
  
x = int(input("Enter X: "))

result = -1
for i in range(n):
    if numbers[i] == x:
        result = i + 1
        break

print(result)
