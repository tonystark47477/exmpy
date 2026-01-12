n = int(input("Enter the number of terms: "))
a=0
b=1
print("Fibanocci series upto" ,n,"terms")
for i in range(n):
    print(a,end="")
    c=a+b
    a=b
    b=c