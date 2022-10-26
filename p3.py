#find area of triangle with 3 sides
import math
a=int(input("enter the value of a= "))
b=int(input("enter the value of b= "))
c=int(input("enter the value of c= "))
s=(a+b+c)/2
area=math.sqrt(s*(s-a)*(s-b)*(s-c))
print("area is = ",area)