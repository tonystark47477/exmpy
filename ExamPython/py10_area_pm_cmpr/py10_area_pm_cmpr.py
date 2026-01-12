class Rectangle:
    def area(self, l, b):
        return l * b

    def perimeter(self, l, b):
        return 2 * (l + b)

    def compare_area(self, a1, a2):
        if a1 > a2:
            return "Rectangle 1 has greater area"
        elif a1 < a2:
            return "Rectangle 2 has greater area"
        else:
            return "Both rectangles have same area"

# Input values
l1 = int(input("Enter length of rectangle 1: "))
b1 = int(input("Enter breadth of rectangle 1: "))

l2 = int(input("Enter length of rectangle 2: "))
b2 = int(input("Enter breadth of rectangle 2: "))

# Object creation
rect = Rectangle()

# Calculations
area1 = rect.area(l1, b1)
area2 = rect.area(l2, b2)

per1 = rect.perimeter(l1, b1)
per2 = rect.perimeter(l2, b2)

# Output
print("\nRectangle 1 Area:", area1)
print("Rectangle 1 Perimeter:", per1)

print("\nRectangle 2 Area:", area2)
print("Rectangle 2 Perimeter:", per2)

# Comparison
result = rect.compare_area(area1, area2)
print("\n" + result)
