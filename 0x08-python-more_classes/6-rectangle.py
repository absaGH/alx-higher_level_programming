#!/usr/bin/python3
"""
Defines a class Rectangle
"""


class Rectangle:
    """Representation of a rectangle 
    Attributes:
        number_of_instances (int): The number of Rectangle instances
    """
    
    number_of_instances = 0
    
    def __init__(self, width=0, height=0):
        """Initializes the rectangle
        Args:
            width (int): The width of the new rectangle
            height (int): The height of the new rectangle
        """
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """gets the private instance attribute width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the private instance attribute width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """gets the private instance attribute height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the private instance attribute height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """returns the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """Return printable string representation of the Rectangle
        The rectangle is represented with the # character
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rectStr = []
        for i in range(self.__height):
            [rectStr.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rectStr.append("\n")
        return ("".join(rectStr))

    def __repr__(self):
        """returns a string representation of the rectangle to be recreated"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """Print a message when an instance of Rectangle is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
