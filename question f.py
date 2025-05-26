values = []

for i in range(5):
    num= int(input(f"Enter number {i + 1}: "))
    values.append(num)

average = sum(values) / len(values)
print(f"the average = ", average)