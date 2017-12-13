#PYTHON FINAL PROJECT
#MAAME YAA OSEI AND PATIENCE TITUS-GLOVER
#GEOMETRY CALCULATOR


#Importing the graphics and math library
from graphics import *
from math import*

#Creating Graphics Window
win = GraphWin("Geometric Calculator", 850,850)
win.setCoords(0,0,20,20)
background = Image(Point(10,10), "geo.gif")
background.draw(win)

#Creating Rectangles for different buttons and backgrounds
#Creating lines for underlining headers

#Quit button
b0=Rectangle(Point(17.5, 2), Point(19.5,3))
b0.setFill("white")
b0.draw(win)
#Perimeter button
b1=Rectangle(Point(0.4,15.5),Point(4.6,16.5))
b1.setFill("white")
b1.draw(win)
#Area button
b2=Rectangle(Point(6,15.5), Point(9,16.5))
b2.setFill("white")
b2.draw(win)
#Volume button
b3=Rectangle(Point(11,15.5), Point(14,16.5))
b3.setFill("white")
b3.draw(win)
#Surface Area button
b4=Rectangle(Point(16,15.5), Point(19,16.5))
b4.setFill("white")
b4.draw(win)
#Square button
b5=Rectangle(Point(1,13), Point(4,14))
b5.setFill("white")
b5.draw(win)
#Rectangle button
b6=Rectangle(Point(6, 13), Point(9,14))
b6.setFill("white")
b6.draw(win)
#Circle button
b7=Rectangle(Point(11, 13), Point(14,14))
b7.setFill("white")
b7.draw(win)
#Triangle button
b8=Rectangle(Point(16,13), Point(19,14))
b8.setFill("white")
b8.draw(win)
#Cuboid button
b9=Rectangle(Point(1,11), Point(4,12))
b9.setFill("white")
b9.draw(win)
#Cylinder button
b10=Rectangle(Point(6, 11), Point(9,12))
b10.setFill("white")
b10.draw(win)
#Pyramid button
b11=Rectangle(Point(11, 11), Point(14,12))
b11.setFill("white")
b11.draw(win)
#Sphere Button
b12=Rectangle(Point(16,11), Point(19,12))
b12.setFill("white")
b12.draw(win)
#Find button
b13 = Rectangle(Point(1,2), Point(4,3))
b13.setFill("white")
b13.draw(win)
#Background 1
b14 = Rectangle(Point(0,18.5), Point(20,20))
b14.setFill("white")
b14.draw(win)
#Background 2
b15 = Rectangle(Point(4.8,17), Point(15, 17.9))
b15.setFill("white")
b15.draw(win)
#Background 3
b16 = Rectangle(Point(6.5, 14.1), Point(13.5, 15.1))
b16.setFill("white")
b16.draw(win)
#Background 4
b17 = Rectangle(Point(2,5), Point(18,11))
b17.setFill("white")
b17.draw(win)
#Underline
l1 = Line(Point(4,18.7), Point(16,18.7))
l1.setFill("red")
l1.draw(win)

                


#Creating text for various headers and buttons in the window

#Quit text
t0=Text(Point(18.5, 2.5), "QUIT")
t0.draw(win)
#Main header text
t1=Text(Point(10,19), "GEOMETRY CALCULATOR")
t1.setFill("red")
t1.setSize(30)
t1.draw(win)
#Sub header text
t2=Text(Point(10,17.5), "What are you calculating for?")
t2.setFill("red")
t2.setSize(20)
t2.draw(win)
#Second sub header text
t3=Text(Point(10,14.5), "For what figure?")
t3.setFill("red")
t3.setSize(20)
t3.draw(win)
#Perimeter/Circumference text
t4= Text(Point(2.5,16), "Perimeter/Circumference")
t4.draw(win)
#Area text
t5=Text(Point(7.5, 16), "Area")
t5.draw(win)
#Volume text
t6= Text(Point(12.5, 16), "Volume")
t6.draw(win)
#Surface Area text
t7= Text(Point(17.5, 16), "Surface Area")
t7.draw(win)
#Square text
t8= Text(Point(2.5,13.5), "Square")
t8.draw(win)
#Rectangle text
t9= Text(Point(7.5, 13.5), "Rectangle")
t9.draw(win)
#Circle text
t10= Text(Point(12.5,13.5), "Cirlce")
t10.draw(win)
#Triagle text
t11=Text(Point(17.5,13.5), "Triangle")
t11.draw(win)
#Cuboid text
t12= Text(Point(2.5, 11.5), "Cuboid")
t12.draw(win)
#Cylinder text
t13= Text(Point(7.5, 11.5), "Cylinder")
t13.draw(win)
#Pyramid text
t14 = Text(Point(12.5, 11.5), "Pyramid")
t14.draw(win)
#Sphere text
t15 = Text(Point(17.5, 11.5), "Sphere")
t15.draw(win)
#Find text
t16 = Text(Point(2.5,2.5), "FIND")
t16.draw(win)

#Creating pop-up prompts, alerts and entry boxes
length = Text(Point(6,10), "Enter a length")
length.setFill("red")
length.setSize(20)
length1 = Text(Point(6,9), "Enter a length")
length1.setFill("red")
length1.setSize(20)
length2 = Text(Point(6,8), "Enter a length")
length2.setFill("red")
length2.setSize(20)
length3 = Text(Point(6,9), "Enter a base length")
length3.setSize(20)
length3.setFill("red")
length4 = Text(Point(6,10), "Enter a base width")
length4.setSize(20)
length4.setFill("red")
space1 = Entry(Point(10,10), 10)
space1.setFill("grey")
width = Text(Point(6,9), "Enter a width")
width.setFill("red")
width.setSize(20)
space2 = Entry(Point(10,9), 10)
space2.setFill("grey")
radius = Text(Point(6,10), "Enter a radius")
radius.setFill("red")
radius.setSize(20)
space3 = Entry(Point(10,8), 10)
space3.setFill("grey")
height = Text(Point(6,8), "Enter a height")
height.setSize(20)
height.setFill("red")
alert1 = Text(Point(10,9), "Cannot find the area of solid figures")
alert1.setSize(15)
alert1.setFill("red")
alert2 = Text(Point(10,9), "Cannot find the volume of a plane figure")
alert2.setSize(15)
alert2.setFill("red")
alert3 = Text(Point(10,9), "Cannot find the surface area of a plane figure")
alert3.setSize(15)
alert3.setFill("red")
alert4 = Text(Point(10,7), "Enter only number(s) please")
alert4.setSize(15)
alert4.setFill("red")
alert5 = Text(Point(10,7), "Enter positive number(s)")
alert5.setSize(15)
alert5.setFill("red")
answer = Text(Point(10,6), "")
answer.setSize(15)
answer.setFill("red")



#Creating classes for various figures with methods to perform calculations
#Sguare class
class Square:
    def __init__(self, length):
        self.length = length

    def getPerimeter(self):
        return round((self.length*4),2)

    def getArea (self):
        return round((self.length**2),2)

#Rectangle class
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def getPerimeter(self):
        return round(((2*self.length)+(2*self.width)),2)

    def getArea (self):
        return round((self.length*self.width),2)

#Circle class
class Circle:
    def __init__ (self, radius):
        self.radius = radius

    def getCircumference(self):
        return round((2*pi*self.radius),2)

    def getArea(self):
        return round((pi*(self.radius**2)),2)

#Triangle class
class Triangle:
    def __init__ (self, length_1, length_2, length_3, height,base):
        self.length_1 = length_1
        self.length_2 = length_2
        self.length_3 = length_3
        self.base = base
        self.height = height
        
    def getPerimeter(self):
        return round(self.length_1+self.length_2+self.length_3,2)

    def getArea(self):
        return round((0.5*self.base*self.height),2)

#Cuboid Class
class Cuboid:
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height

    def getPerimeter(self):
        return round((2*((2*self.length)+(2*self.width))+(4*(2*self.height)+(2*self.width))),2)

    def getVolume(self):
        return round((self.length*self.width*self.height),2)

    def getSurfaceArea(self):
        return round(((2*(self.length*self.width))+(4*(self.height*self.width))),2)
    
#Cylinder Class
class Cylinder:
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def getPerimeter(self):
        return round((2*(pi*(2*self.radius)+self.height)),2)

    def getVolume(self):
        return round((pi*(self.radius**2)*self.height),2)

    def getSurfaceArea(self):
        return round(((2*pi*self.radius*self.height)+(pi*(self.radius**2)*self.height)),2)
    
#Pyramid Class
class Pyramid:
    def __init__(self, height,base_length, base_width):
        self.height = height
        self.length = base_length
        self.width = base_width

    def getPerimeter(self):
        return round(((((sqrt((self.length**2)+(self.width**2)))/2)*4)+(2*self.length)+(2*self.width)),2)

    def getVolume(self):
        return round((self.length*self.width*self.height)/3 ,2)

    def getSurfaceArea(self):
        return round((self.length*self.width)+(self.length*sqrt((self.width/2)**2+self.height**2))+(self.width*sqrt((self.length/2)**2+self.height**2)),2)

#Sphere Class
class Sphere:
    def __init__ (self, radius):
        self.radius = radius

    def getPerimeter(self):
        return round(2*pi*(self.radius**2),2)

    def getVolume(self):
        return round((4/3)*pi*(self.radius)**3,2)

    def getSurfaceArea(self):
        return round(4*pi*(self.radius)**2,2)
    
        

#Creating a varialble for a click in the window
p = win.getMouse()
#Creating a loop to make the program run as long as the user hasn't clicked on quit
while (not (17.5<=p.x<=19.5 and 2<=p.y<=3)):
#Perimeter Calculations
    #Perimeter of a square
    if 0.4<=p.x<=4.6 and 15.5<=p.y<=16.5:
        b1.setFill("yellow")
        p =win.getMouse()
        if 1<=p.x<=4 and 13<=p.y<=14:
            b5.setFill("yellow")
            radius.undraw()
            height.undraw()
            length.undraw()
            length1.undraw()
            length2.undraw()
            length3.undraw()
            length4.undraw()
            alert1.undraw()
            alert2.undraw()
            alert3.undraw()
            alert4.undraw()
            alert5.undraw()
            width.undraw()
            space2.undraw()
            space3.undraw()
            space1.undraw()
            answer.undraw()
            length.draw(win)
            space1.draw(win)
            p = win.getMouse()
            if 1<=p.x<=4 and 2<=p.y<=3:
                b1.setFill("white")
                b5.setFill("white")
                try:
                    square_length = eval(space1.getText())
                    if square_length<0:
                        alert5.draw(win)
                    else: 
                        square = Square(square_length)
                        square_perimeter = square.getPerimeter()
                        answer.setText(square_perimeter)
                        answer.draw(win)
                        space1.setText("")
                except NameError:
                    alert4.draw(win)
                except SyntaxError:
                    alert4.draw(win)
            
            
        #Perimeter of a Rectangle    
        elif 6<=p.x<=9 and 13<=p.y<=14:
            b6.setFill("yellow")
            radius.undraw()
            height.undraw()
            length.undraw()
            length1.undraw()
            length2.undraw()
            length3.undraw()
            length4.undraw()
            width.undraw()
            space2.undraw()
            space3.undraw()
            space1.undraw()
            alert1.undraw()
            alert2.undraw()
            alert3.undraw()
            alert4.undraw()
            alert5.undraw()
            answer.undraw()
            length.draw(win)
            width.draw(win)
            space1.draw(win)
            space2.draw(win)
            p= win.getMouse()
            try:
                if 1<=p.x<=4 and 2<=p.y<=3:
                    b13.setFill("yellow")
                    b1.setFill("white")
                    b6.setFill("white")
                    rectangle_length = eval(space1.getText())
                    rectangle_width = eval(space2.getText())
                    if rectangle_length<0 or rectangle_width<0:
                        alert5.draw(win)
                    else:
                        rectangle = Rectangle(rectangle_length, rectangle_width)
                        rectangle_perimeter = rectangle.getPerimeter()
                        answer.setText(rectangle_perimeter)
                        answer.draw(win)
                        space1.setText("")
                        space2.setText("")
            except NameError:
                alert4.draw(win)
            except SyntaxError:
                alert4.draw(win)

        #Circumference of a circle    
        elif  11<=p.x<=14 and 13<=p.y<=14:
            radius.undraw()
            height.undraw()
            length.undraw()
            length1.undraw()
            length2.undraw()
            length3.undraw()
            length4.undraw()
            width.undraw()
            space2.undraw()
            space3.undraw()
            space1.undraw()
            alert1.undraw()
            alert2.undraw()
            alert3.undraw()
            alert4.undraw()
            alert5.undraw()
            answer.undraw()
            radius.draw(win)
            space1.draw(win)
            p=win.getMouse()
            try:
                if 1<=p.x<=4 and 2<=p.y<=3:
                    circle_radius = eval(space1.getText())
                    if circle_radius<0:
                        alert5.draw(win)
                    else:
                        circle = Circle(circle_radius)
                        circle_circumference=circle.getCircumference()
                        answer.setText(circle_circumference)
                        answer.draw(win)
                        space1.setText("")
            except NameError:
                alert4.draw(win)
            except SyntaxError:
                alert4.draw(win)
                
        #Perimeter of a Triangle            
        elif 16<=p.x<=19 and 13<=p.y<=14:
            radius.undraw()
            height.undraw()
            length.undraw()
            length1.undraw()
            length2.undraw()
            length3.undraw()
            length4.undraw()
            width.undraw()
            space2.undraw()
            space3.undraw()
            space1.undraw()
            alert1.undraw()
            alert2.undraw()
            alert3.undraw()
            alert4.undraw()
            alert5.undraw()
            answer.undraw()
            length.draw(win)
            length1.draw(win)
            length2.draw(win)
            space1.draw(win)
            space2.draw(win)
            space3.draw(win)
            p = win.getMouse()
            try:
                if 1<=p.x<=4 and 2<=p.y<=3:
                    triangle_firstside = eval(space1.getText())
                    triangle_secondside = eval(space2.getText())
                    triangle_thirdside = eval(space3. getText())
                    if triangle_firstside<0 or triangle_secondside<0 or triangle_thirdside<0:
                        alert5.draw(win)
                    else:
                        triangle = Triangle(triangle_firstside, triangle_secondside, triangle_thirdside)
                        triangle_perimeter = triangle.getPerimeter()
                        answer.setText(triangle_perimeter)
                        answer.draw(win)
                        space1.setText("")
                        space2.setText("")
                        space3.setText("")
            except NameError:
                alert4.draw(win)
            except SyntaxError:
                alert4.draw(win)
                    
        #Perimeter of a cuboid
        elif 1<=p.x<=4 and 11<=p.y<=12:
            radius.undraw()
            height.undraw()
            length.undraw()
            length1.undraw()
            length2.undraw()
            length3.undraw()
            length4.undraw()
            width.undraw()
            space2.undraw()
            space3.undraw()
            space1.undraw()
            alert1.undraw()
            alert2.undraw()
            alert3.undraw()
            alert4.undraw()
            alert5.undraw()
            answer.undraw()
            length.draw(win)
            width.draw(win)
            height.draw(win)
            space1.draw(win)
            space2.draw(win)
            space3.draw(win)
            p= win.getMouse()
            try:
                if 1<=p.x<=4 and 2<=p.y<=3:
                    cuboid_length = eval(space1.getText())
                    cuboid_width = eval(space2.getText())
                    cuboid_height = eval(space3.getText())
                    if cuboid_length<0 or cuboid_width<0 or cuboid_height<0:
                        alert5.draw(win)
                    else:
                        cuboid = Cuboid(cuboid_length, cuboid_width, cuboid_height)
                        cuboid_perimeter = cuboid.getPerimeter()
                        answer.setText(cuboid_perimeter)
                        answer.draw(win)
                        space1.setText("")
                        space2.setText("")
                        space3.setText("")
            except NameError:
                alert4.draw(win)
            except SyntaxError:
                alert4.draw(win)
                
        #Perimeter of a cylinder
        elif 6<=p.x<=9 and 11<=p.y<=12:
            radius.undraw()
            height.undraw()
            length.undraw()
            length1.undraw()
            length2.undraw()
            length3.undraw()
            length4.undraw()
            width.undraw()
            space2.undraw()
            space3.undraw()
            space1.undraw()
            alert1.undraw()
            alert2.undraw()
            alert3.undraw()
            alert5.undraw()
            alert4.undraw()
            answer.undraw()
            radius.draw(win)
            height.draw(win)
            space1.draw(win)
            space3.draw(win)
            p=win.getMouse()
            try:
                if 1<=p.x<=4 and 2<=p.y<=3:
                    cylinder_radius = eval(space1.getText())
                    cylinder_height = eval(space3.getText())
                    if cylinder_radius<0 or cylinder_height<0:
                        alert5.draw(win)
                    else:
                        cylinder = Cylinder(cylinder_radius, cylinder_height)
                        cylinder_perimeter =cylinder.getPerimeter()
                        answer.setText(cylinder_perimeter)
                        answer.draw(win)
                        space1.setText("")
                        space3.setText("")
            except NameError:
                alert4.draw(win)
            except SyntaxError:
                alert4.draw(win)
        
        #Perimeter of a Pyramid
        elif 11<=p.x<=14 and 11<=p.y<=12:
            radius.undraw()
            height.undraw()
            length.undraw()
            length1.undraw()
            length2.undraw()
            length3.undraw()
            length4.undraw()
            width.undraw()
            space2.undraw()
            space3.undraw()
            space1.undraw()
            alert1.undraw()
            alert2.undraw()
            alert3.undraw()
            alert4.undraw()
            alert5.undraw()
            answer.undraw()
            length3.draw(win)
            length4.draw(win)
            space1.draw(win)
            space2.draw(win)
            height.draw(win)
            space3.draw(win)
            p = win.getMouse()
            try:
                if 1<=p.x<=4 and 2<=p.y<=3:
                    pyramid_width = eval(space1.getText())
                    pyramid_length = eval(space2.getText())
                    pyramid_height = eval(space3.getText())
                    if pyramid_width<0 or pyramid_length<0 or pyramid_height<0:
                        alert5.draw(win)
                    else:
                        pyramid = Pyramid(pyramid_height, pyramid_length, pyramid_width)
                        pyramid_perimeter =pyramid.getPerimeter()
                        answer.setText(pyramid_perimeter)
                        answer.draw(win)
                        space1.setText("")
                        space2.setText("")
                        space3.setText("")
            except NameError:
                alert4.draw(win)
            except SyntaxError:
                alert4.draw(win)
                    
                    
        #Circumference of a sphere
        elif 16<=p.x<=19 and 11<=p.y<=12:
            radius.undraw()
            height.undraw()
            length.undraw()
            length1.undraw()
            length2.undraw()
            length3.undraw()
            length4.undraw()
            width.undraw()
            space2.undraw()
            space3.undraw()
            space1.undraw()
            alert1.undraw()
            alert2.undraw()
            alert3.undraw()
            alert4.undraw()
            alert5.undraw()
            answer.undraw()
            radius.draw(win)
            space1.draw(win)
            p = win.getMouse()
            try:
                if 1<=p.x<=4 and 2<=p.y<=3:
                    sphere_radius = eval(space1.getText())
                    if sphere_radius<0:
                        alert5.draw(win)
                    else:
                        sphere = Sphere(sphere_radius)
                        sphere_perimeter= sphere.getPerimeter()
                        answer.setText(sphere_perimeter)
                        answer.draw(win)
                        space1.setText("")
            except NameError:
                alert4.draw(win)
            except SyntaxError:
                alert4.draw(win)

    #Area Calculations        
    elif 6<=p.x<=9 and 15.5<=p.y<=16.5:
        p= win.getMouse()

        #Area  of a square
        if 1<=p.x<=4 and 13<=p.y<=14:
            radius.undraw()
            height.undraw()
            length.undraw()
            length1.undraw()
            length2.undraw()
            length3.undraw()
            length4.undraw()
            width.undraw()
            space2.undraw()
            space3.undraw()
            space1.undraw()
            alert1.undraw()
            alert2.undraw()
            alert3.undraw()
            alert4.undraw()
            alert5.undraw()
            answer.undraw()
            length.draw(win)
            space1.draw(win)
            p=win.getMouse()
            try:
                if 1<=p.x<=4 and 2<=p.y<=3:
                    square2_length = eval(space1.getText())
                    if square2_length<0:
                        alert5.draw(win)
                    else:
                        square2 = Square(square2_length)
                        square2_area = square2.getArea()
                        answer.setText(square2_area)
                        answer.draw(win)
                        space1.setText("")
            except NameError:
                alert4.draw(win)

        #Area of a rectangle    
        elif 6<=p.x<=9 and 13<=p.y<=14:
            radius.undraw()
            height.undraw()
            length.undraw()
            length1.undraw()
            length2.undraw()
            length3.undraw()
            length4.undraw()
            width.undraw()
            space2.undraw()
            space3.undraw()
            space1.undraw()
            alert1.undraw()
            alert2.undraw()
            alert3.undraw()
            alert4.undraw()
            alert5.undraw()
            answer.undraw()
            length.draw(win)
            width.draw(win)
            space1.draw(win)
            space2.draw(win)
            p=win.getMouse()
            try:
                if 1<=p.x<=4 and 2<=p.y<=3:
                    rectangle2_length = eval(space1.getText())
                    rectangle2_width = eval(space2.getText())
                    if rectangle2_length<0 or rectangle2_width<0:
                        alert5.draw(win)
                    else:
                        rectangle2 = Rectangle(rectangle2_length, rectangle2_width)
                        rectangle2_area = rectangle2.getArea()
                        answer.setText(rectangle2_area)
                        answer.draw(win)
                        space1.setText("")
                        space2.setText("")
            except NameError:
                alert4.draw(win)
            except SyntaxError:
                alert4.draw(win)
            
                    
        #Area of a circle    
        elif  11<=p.x<=14 and 13<=p.y<=14:
            radius.undraw()
            height.undraw()
            length.undraw()
            length1.undraw()
            length2.undraw()
            length3.undraw()
            length4.undraw()
            width.undraw()
            alert1.undraw()
            alert2.undraw()
            alert3.undraw()
            alert4.undraw()
            alert5.undraw()
            answer.undraw()
            space2.undraw()
            space3.undraw()
            space1.undraw()
            radius.draw(win)
            space1.draw(win)
            p = win.getMouse()
            try:
                if 1<=p.x<=4 and 2<=p.y<=3:
                    radius2 = eval(space1.getText())
                    if radius2<0:
                        alert5.draw(win)
                    else:
                        circle2 = Circle(radius2)
                        circle2_area = circle2.getArea()
                        answer.setText(circle2_area)
                        answer.draw(win)
                        space1.setText("")
            except NameError:
                alert4.draw(win)
            except SyntaxError:
                alert4.draw(win)

        #Area of a triangle
        elif 16<=p.x<=19 and 13<=p.y<=14:
            radius.undraw()
            height.undraw()
            length.undraw()
            length1.undraw()
            length2.undraw()
            length3.undraw()
            length4.undraw()
            width.undraw()
            space2.undraw()
            space3.undraw()
            space1.undraw()
            alert1.undraw()
            alert2.undraw()
            alert3.undraw()
            alert4.undraw()
            alert5.undraw()
            answer.undraw()
            height.draw(win)
            length3.draw(win)
            space2.draw(win)
            space3.draw(win)
            p = win.getMouse()
            try:
                if 1<=p.x<=4 and 2<=p.y<=3:
                    base_2= eval(space2.getText())
                    height_2 = eval(space3.getText())
                    length_1 = 1
                    length_2 = 1
                    length_3 = 1
                    if base_2<0 or height_2<0:
                        alert5.draw(win)
                    else:
                        triangle2 = Triangle(length_1, length_2, length_3, height_2, base_2)
                        triangle2_area = triangle2.getArea()
                        answer.setText(triangle2_area)
                        answer.draw(win)
                        space2.setText("")
                        space3.setText("")
            except NameError:
                alert4.draw(win)
            except SyntaxError:
                alert4.draw(win)
                
        #Area of solid figures cannot be calculated
        elif 1<=p.x<=4 and 11<=p.y<=12:
            radius.undraw()
            height.undraw()
            length.undraw()
            length1.undraw()
            length2.undraw()
            length3.undraw()
            length4.undraw()
            width.undraw()
            space2.undraw()
            space3.undraw()
            space1.undraw()
            alert4.undraw()
            alert5.undraw()
            answer.undraw()
            alert1.undraw()
            alert2.undraw()
            alert3.undraw()
            alert1.draw(win)


        elif 6<=p.x<=9 and 11<=p.y<=12:
            radius.undraw()
            height.undraw()
            length.undraw()
            length1.undraw()
            length2.undraw()
            length3.undraw()
            length4.undraw()
            width.undraw()
            space2.undraw()
            space3.undraw()
            space1.undraw()
            alert4.undraw()
            alert5.undraw()
            answer.undraw()
            alert1.undraw()
            alert2.undraw()
            alert3.undraw()
            alert1.draw(win)

        elif 11<=p.x<=14 and 11<=p.y<=12:
            radius.undraw()
            height.undraw()
            length.undraw()
            length1.undraw()
            length2.undraw()
            length3.undraw()
            length4.undraw()
            width.undraw()
            space2.undraw()
            space3.undraw()
            space1.undraw()
            alert4.undraw()
            alert5.undraw()
            answer.undraw()
            alert1.undraw()
            alert2.undraw()
            alert3.undraw()
            alert1.draw(win)

        elif 16<=p.x<=19 and 11<=p.y<=12:
            radius.undraw()
            height.undraw()
            length.undraw()
            length1.undraw()
            length2.undraw()
            length3.undraw()
            length4.undraw()
            width.undraw()
            space2.undraw()
            space3.undraw()
            space1.undraw()
            alert4.undraw()
            alert5.undraw()
            answer.undraw()
            alert1.undraw()
            alert2.undraw()
            alert3.undraw()
            alert1.draw(win)

    #Volume Calculations        
    elif 11<=p.x<=14 and 15.5<=p.y <=16.5:
        p= win.getMouse()
        
        #Volume of plane figures cannot be calculated
        if 1<=p.x<=4 and 13<=p.y<=14:
            radius.undraw()
            height.undraw()
            length.undraw()
            length1.undraw()
            length2.undraw()
            length3.undraw()
            length4.undraw()
            width.undraw()
            space2.undraw()
            space3.undraw()
            space1.undraw()
            alert4.undraw()
            alert5.undraw()
            answer.undraw()
            alert1.undraw()
            alert2.undraw()
            alert3.undraw()
            alert2.draw(win)

            
        elif 6<=p.x<=9 and 13<=p.y<=14:
            radius.undraw()
            height.undraw()
            length.undraw()
            length1.undraw()
            length2.undraw()
            length3.undraw()
            length4.undraw()
            width.undraw()
            space2.undraw()
            space3.undraw()
            space1.undraw()
            alert1.undraw()
            alert2.undraw()
            alert3.undraw()
            alert2.draw(win)

            
        elif  11<=p.x<=14 and 13<=p.y<=14:
            radius.undraw()
            height.undraw()
            length.undraw()
            length1.undraw()
            length2.undraw()
            length3.undraw()
            length4.undraw()
            width.undraw()
            space2.undraw()
            space3.undraw()
            space1.undraw()
            alert4.undraw()
            alert5.undraw()
            answer.undraw()
            alert1.undraw()
            alert2.undraw()
            alert3.undraw()
            alert2.draw(win)


        elif 16<=p.x<=19 and 13<=p.y<=14:
            radius.undraw()
            height.undraw()
            length.undraw()
            length1.undraw()
            length2.undraw()
            length3.undraw()
            length4.undraw()
            width.undraw()
            space2.undraw()
            space3.undraw()
            space1.undraw()
            alert4.undraw()
            alert5.undraw()
            answer.undraw()
            alert1.undraw()
            alert2.undraw()
            alert3.undraw()
            alert2.draw(win)

        #Volume of a cuboid
        elif 1<=p.x<=4 and 11<=p.y<=12:
            radius.undraw()
            height.undraw()
            length.undraw()
            length1.undraw()
            length2.undraw()
            length3.undraw()
            length4.undraw()
            width.undraw()
            space2.undraw()
            space3.undraw()
            space1.undraw()
            alert4.undraw()
            alert5.undraw()
            answer.undraw()
            length.draw(win)
            width.draw(win)
            height.draw(win)
            space1.draw(win)
            space2.draw(win)
            space3.draw(win)
            p=win.getMouse()
            try:
                if 1<=p.x<=4 and 2<=p.y<=3:
                    cuboid2_length=eval(space1.getText())
                    cuboid2_width=eval(space2.getText())
                    cuboid2_height=eval(space3.getText())
                    if cuboid2_length<0 or cuboid2_width<0 or cuboid2_height<0:
                        alert5.draw(win)
                    else:
                        cuboid2= Cuboid(cuboid2_length,cuboid2_width,cuboid2_height)
                        cuboid2_volume=cuboid2.getVolume()
                        answer.setText(cuboid2_volume)
                        answer.draw(win)
                        space1.setText("")
                        space2.setText("")
                        space3.setText("")
            except NameError:
                alert4.draw(win)
            except SyntaxError:
                alert4.draw(win)
                    
        #Volume of a cylinder
        elif 6<=p.x<=9 and 11<=p.y<=12:
            radius.undraw()
            height.undraw()
            length.undraw()
            length1.undraw()
            length2.undraw()
            length3.undraw()
            length4.undraw()
            width.undraw()
            space2.undraw()
            space3.undraw()
            space1.undraw()
            alert4.undraw()
            alert5.undraw()
            answer.undraw()
            radius.draw(win)
            height.draw(win)
            space1.draw(win)
            space3.draw(win)
            p=win.getMouse()
            try:
                if 1<=p.x<=4 and 2<=p.y<=3:
                    cylinder2_radius=eval(space1.getText())
                    cylinder2_height=eval(space3.getText())
                    if cylinder2_radius<0  or cylinder2_height<0:
                        alert5.draw(win)
                    else:
                        cylinder2= Cylinder(cylinder2_radius,cylinder2_height)
                        cylinder2_volume=cylinder2.getVolume()
                        answer.setText(cylinder2_volume)
                        answer.draw(win)
                        space1.setText("")
                        space3.setText("")
            except NameError:
                alert4.draw(win)
            except SyntaxError:
                alert4.draw(win)
                    
            
        #Volume of a pyramid
        elif 11<=p.x<=14 and 11<=p.y<=12:
            radius.undraw()
            height.undraw()
            length.undraw()
            length1.undraw()
            length2.undraw()
            length3.undraw()
            length4.undraw()
            width.undraw()
            space2.undraw()
            space3.undraw()
            space1.undraw()
            alert4.undraw()
            alert5.undraw()
            answer.undraw()
            length3.draw(win)
            length4.draw(win)
            space1.draw(win)
            space2.draw(win)
            height.draw(win)
            space3.draw(win)
            p=win.getMouse()
            try:
                if 1<=p.x<=4 and 2<=p.y<=3:
                    pyramid2_width=eval(space1.getText())
                    pyramid2_height=eval(space3.getText())
                    pyramid2_length=eval(space2.getText())
                    if pyramid2_width<0  or pyramid2_height<0 or pyramid2_length<0:
                        alert5.draw(win)
                    else:
                        pyramid2= Pyramid(pyramid2_height, pyramid2_length, pyramid2_width)
                        pyramid2_volume=pyramid2.getVolume()
                        answer.setText(pyramid2_volume)
                        answer.draw(win)
                        space1.setText("")
                        space2.setText("")
                        space3.setText("")
            except NameError:
                alert4.draw(win)
            except SyntaxError:
                alert4.draw(win)
                    
        #Volume of a sphere
        elif 16<=p.x<=19 and 11<=p.y<=12:
            radius.undraw()
            height.undraw()
            length.undraw()
            length1.undraw()
            length2.undraw()
            length3.undraw()
            length4.undraw()
            width.undraw()
            space2.undraw()
            space3.undraw()
            space1.undraw()
            alert4.undraw()
            alert5.undraw()
            answer.undraw()
            radius.draw(win)
            space1.draw(win)
            p = win.getMouse()
            p=win.getMouse()
            try:
                if 1<=p.x<=4 and 2<=p.y<=3:
                    sphere2_radius=eval(space1.getText())
                    if sphere2_radius<0:
                        alert5.draw(win)
                    else:
                        sphere2= Sphere(sphere2_radius)
                        sphere2_volume=sphere2.getVolume()
                        answer.setText(sphere2_volume)
                        answer.draw(win)
                        space1.setText("")
            except NameError:
                alert4.draw(win)
            except SyntaxError:
                alert4.draw(win)
                    


    #Surface Area Calculations
    elif 16<=p.x<=19 and 15.5<=p.y<=16.5:
        p= win.getMouse()

        #Suraface Area of plane figures cannot be calculated
        if 1<=p.x<=4 and 13<=p.y<=14:
            radius.undraw()
            height.undraw()
            length.undraw()
            length1.undraw()
            length2.undraw()
            length3.undraw()
            length4.undraw()
            width.undraw()
            space2.undraw()
            space3.undraw()
            space1.undraw()
            alert4.undraw()
            alert5.undraw()
            answer.undraw()
            alert1.undraw()
            alert2.undraw()
            alert3.undraw()
            alert3.draw(win)

            
        elif 6<=p.x<=9 and 13<=p.y<=14:
            radius.undraw()
            height.undraw()
            length.undraw()
            length1.undraw()
            length2.undraw()
            length3.undraw()
            length4.undraw()
            width.undraw()
            space2.undraw()
            space3.undraw()
            space1.undraw()
            alert4.undraw()
            alert5.undraw()
            answer.undraw()
            alert1.undraw()
            alert2.undraw()
            alert3.undraw()
            alert3.draw(win)

            
        elif  11<=p.x<=14 and 13<=p.y<=14:
            radius.undraw()
            height.undraw()
            length.undraw()
            length1.undraw()
            length2.undraw()
            length3.undraw()
            length4.undraw()
            width.undraw()
            space2.undraw()
            space3.undraw()
            space1.undraw()
            alert4.undraw()
            alert5.undraw()
            answer.undraw()
            alert1.undraw()
            alert2.undraw()
            alert3.undraw()
            alert3.draw(win)


        elif 16<=p.x<=19 and 13<=p.y<=14:
            radius.undraw()
            height.undraw()
            length.undraw()
            length1.undraw()
            length2.undraw()
            length3.undraw()
            length4.undraw()
            width.undraw()
            space2.undraw()
            space3.undraw()
            space1.undraw()
            alert4.undraw()
            alert5.undraw()
            answer.undraw()
            alert1.undraw()
            alert2.undraw()
            alert3.undraw()
            alert3.draw(win)

        #Surface area of a cuboid
        elif 1<=p.x<=4 and 11<=p.y<=12:
            radius.undraw()
            height.undraw()
            length.undraw()
            length1.undraw()
            length2.undraw()
            length3.undraw()
            length4.undraw()
            width.undraw()
            space2.undraw()
            space3.undraw()
            space1.undraw()
            alert1.undraw()
            alert2.undraw()
            alert3.undraw()
            alert4.undraw()
            alert5.undraw()
            answer.undraw()
            length.draw(win)
            width.draw(win)
            height.draw(win)
            space1.draw(win)
            space2.draw(win)
            space3.draw(win)
            p=win.getMouse()
            try:
                if 1<=p.x<=4 and 2<=p.y<=3:
                    cuboid3_length=eval(space1.getText())
                    cuboid3_width = eval(space2.getText())
                    cuboid3_height=eval(space3.getText())
                    if cuboid3_length<0  or cuboid3_height<0 or cuboid3_width<0:
                        alert5.draw(win)
                    else:
                        cuboid3=Cuboid(cuboid3_length, cuboid3_width, cuboid3_height)
                        cuboid3_sArea=cuboid3.getSurfaceArea()
                        answer.setText(cuboid3_sArea)
                        answer.draw(win)
                        space1.setText("")
                        space2.setText("")
                        space3.setText("")
            except NameError:
                alert4.draw(win)
            except SyntaxError:
                alert4.draw(win)
                    
        #Surface Area of a cylinder
        elif 6<=p.x<=9 and 11<=p.y<=12:
            radius.undraw()
            height.undraw()
            length.undraw()
            length1.undraw()
            length2.undraw()
            length3.undraw()
            length4.undraw()
            width.undraw()
            space2.undraw()
            space3.undraw()
            space1.undraw()
            alert1.undraw()
            alert2.undraw()
            alert3.undraw()
            alert4.undraw()
            alert5.undraw()
            answer.undraw()
            radius.draw(win)
            height.draw(win)
            space1.draw(win)
            space3.draw(win)
            p=win.getMouse()
            try:
                if 1<=p.x<=4 and 2<=p.y<=3:
                    cylinder3_radius=eval(space1.getText())
                    cylinder3_height=eval(space3.getText())
                    if cylinder3_radius<0  or cylinder3_height<0:
                        alert5.draw(win)
                    else:
                        cylinder3= Cylinder(cylinder3_radius,cylinder3_height)
                        cylinder3_sArea=cylinder3.getSurfaceArea()
                        answer.setText(cylinder3_sArea)
                        answer.draw(win)
                        space1.setText("")
                        space3.setText("")
            except NameError:
                alert4.draw(win)
            except SyntaxError:
                alert4.draw(win)
                    
        #Surface Area of a Pyramid
        elif 11<=p.x<=14 and 11<=p.y<=12:
            radius.undraw()
            height.undraw()
            length.undraw()
            length1.undraw()
            length2.undraw()
            length3.undraw()
            length4.undraw()
            width.undraw()
            space2.undraw()
            space3.undraw()
            space1.undraw()
            alert4.undraw()
            alert1.undraw()
            alert2.undraw()
            alert3.undraw()
            alert5.undraw()
            answer.undraw()
            length3.draw(win)
            length4.draw(win)
            space1.draw(win)
            space2.draw(win)
            height.draw(win)
            space3.draw(win)
            p=win.getMouse()
            try:
                if 1<=p.x<=4 and 2<=p.y<=3:
                    pyramid3_width= eval(space1.getText())
                    pyramid3_length = eval(space2.getText())
                    pyramid3_height= eval(space3.getText())
                    if pyramid3_width<0  or pyramid3_length<0 or pyramid3_height<0:
                        alert5.draw(win)
                    else:
                        pyramid3= Pyramid(pyramid3_height, pyramid3_length, pyramid3_width)
                        pyramid3_sArea=pyramid3.getSurfaceArea()
                        answer.setText(pyramid3_sArea)
                        answer.draw(win)
                        space1.setText("")
                        space2.setText("")
                        space3.setText("")
            except NameError:
                alert4.draw(win)
            except SyntaxError:
                alert4.draw(win)
                    
        #Surface Area of a Sphere
        elif 16<=p.x<=19 and 11<=p.y<=12:
            radius.undraw()
            height.undraw()
            length.undraw()
            length1.undraw()
            length2.undraw()
            length3.undraw()
            length4.undraw()
            width.undraw()
            space2.undraw()
            space3.undraw()
            space1.undraw()
            alert4.undraw()
            alert1.undraw()
            alert2.undraw()
            alert3.undraw()
            alert5.undraw()
            answer.undraw()
            radius.draw(win)
            space1.draw(win)
            p = win.getMouse()
            try:
                if 1<=p.x<=4 and 2<=p.y<=3:
                    sphere3_radius=eval(space1.getText())
                    if sphere3_radius<0:
                        alert5.draw(win)
                    else:
                        sphere3= Sphere(sphere3_radius)
                        sphere3_sArea=sphere3.getSurfaceArea()
                        answer.setText(sphere3_sArea)
                        answer.draw(win)
                        space1.setText("")
            except NameError:
                alert4.draw(win)
            except SyntaxError:
                alert4.draw(win)
                        
    p= win.getMouse()           
else:
    #Close window if user clicks on quit button
    win.close()


