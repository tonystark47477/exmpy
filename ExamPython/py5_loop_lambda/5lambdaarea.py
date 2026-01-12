area_sq = lambda s: s*s
area_rec = lambda l,b: l*b
area_tri = lambda b,h: 0.5*b*h

sqside=int(input("Enter the length of the square:"))
print("Area of the square is: ",area_sq(sqside))

reclength=int(input("Enter the length of the rectangle: "))
recbreadth=int(input("Enter the breadth of the rectangle: "))
print("Area of the rectangle is: ",area_rec(reclength,recbreadth))

trilength=int(input("Enter the length of the triangle: "))
tribreadth=int(input("Enter the breadth of the triangle: "))
print("Area of the triangle is: ",area_tri(trilength,tribreadth))