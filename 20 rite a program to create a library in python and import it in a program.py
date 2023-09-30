#Write a program to create a library in python and import it in a program.
#Rect.py
class Rectangle:
    def __init__(self):
        print("Rectangle")

    def Area(self, length, width):
        self.l=length
        self.w=width
        print("Area of Rectangle is : ", self.l*self.w)

#Sq.py
class Square:
    def __init__(self):
        print("Square")
    def Area(self, side):
        self.a=side
        print("Area of square is : ", self.a*self.a)

#Tri.py
class Triangle:
    def __init__(self):
        print("Trinagle")

    def Area(self, base, height):
        self.b=base
        self.h=height
        ar= (1/2)*self.b*self.h
        print("Area of Triangle is : ", ar )

#main.py
from Shape import Rect
from Shape import Sq
from Shape import Tri

r=Rect.Rectangle( ) #Create an object r for Rectangle class
r.Area(10,20) # Call the module Area( ) of Rectangle class by passing
argument

s=Sq.Square( ) #Create an object s for Square class
s.Area(10) # Call the module Area( ) of Square class by passing argument

t=Tri.Triangle( ) #Create an object t for Triangle class
t.Area(6,8) # Call the module Area( ) of Triangle class by passing argument
