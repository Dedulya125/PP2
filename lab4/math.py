#Ex 1
import math

radius = int(input())
pi = math.pi

print(radius * pi / 180)

#Ex 2
import math

height = int(input())
b1 = int(input())
b2 = int(input())

a = ((b1+b2)/2)*height

print("Area: ",a)

#Ex 3
import math 

sides = int(input("Number of sides: "))
length = int(input("Length of sides: "))

area = (sides * length**2) / (4 * math.tan(math.pi/sides))

print(int(area))

#Ex 4
import math

l = int(input())
h = int(input())

print(float(h*l))