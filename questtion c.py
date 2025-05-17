def calculate_area (length):
    return length * length

def calculate_perimeter(length):
    return 4*length
    
length = float(input("Enter the length of the square: "))

area = calculate_area(length)
perimeter = calculate_perimeter(length)

print("The area of the square is = ", area)
print("The perimeter of the square is = ", perimeter)
   
