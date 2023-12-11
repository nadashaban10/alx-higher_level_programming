#!/usr/bin/python3
'''define a rectanale class inhertis'''
from models.base import Base


class Rectangle(Base):
    '''
        instance Methodes of rectangle
        Display()
        Area()
        Update()
        __str__()

    '''
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

        '''
        initialize the attribute instance

        Args:



        '''
    @property
    def width(self):
        """Set/get the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Set/get the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Set/get the x coordinate of the Rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Set/get the y coordinate of the Rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        '''calculate area of rectanale'''
        return self.__width * self.__height

    def display(self):
        '''Print the Rectangle using the `#` character.'''
        if self.width == 0 or self.height == 0:
            print("")
            return
        for i in range(self.__y):
            print('')
        for row in range(self.__height):
            for j in range(self.__x):
                print(" ", end="")
            for col in range(self.__width):
                print('#', end="")
            print()

    def update(self, *args, **kwargs):
        '''Update with args and kwargs


        Args:
            (id) 1st-attribute.
            (width) 2nd-attribute.
            (height) 3nd-attribute.
            (x) 4nd-attribute.
            (y) 5nd-attribute.

        '''
        if args is not None and len(args) != 0:
            if len(args) >= 1:
                if type(args[0]) != int and args[0] is not None:
                    raise TypeError("id must be an integer")
                self.id = args[0]
            if len(args) > 1:
                self.width = args[1]
            if len(args) > 2:
                self.height = args[2]
            if len(args) > 3:
                self.x = args[3]
            if len(args) > 4:
                self.y = args[4]
        else:
            for key, value in kwargs.items():
                    if key == "id":
                        if type(value) != int and value is not None:
                            raise TypeError("id must be an integer")
                        self.id = value
                    if key == "width":
                        self.width = value
                    if key == "height":
                        self.height = value
                    if key == "x":
                        self.x = value
                    if key == "y":
                        self.y = value


    def __str__(self):
        return (f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}")
