a=eval(input("Enter the length of the first side of the triangle: "))
b=eval(input("Enter the length of the second side of the triangle: "))
c=eval(input("Enter the length of the third side of the triangle: "))
s=(a+b+c)/2
p=a+b+c
area=(s*(s-a)*(s-b)*(s-c))**0.5
print("The semiperimeter is",s) 
print("The perimeter is",p)
print("The area is",area)
