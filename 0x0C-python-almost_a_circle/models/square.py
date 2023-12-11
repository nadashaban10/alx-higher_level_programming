#!/usr/bin/python3
'''class square (rectanagle) inherits'''
from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        '''
        Initialize a new square object.

        Args:
            size: The side length of the square.
            x: The X of the square.
            y: The Y of the square.
            id: ID of the square.
        '''
        self.size = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''
            string representation of the square
            Returns:
            A string of the format "[Square] (<id>) <x>/<y> - <size>".
        '''
        return f"[square] ({self.id}) ({self.x})/({self.y}) - {self.width}"

    @property
    def size(self):
        """
        Retrieves the size attribute
        """
        return self.__Width

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
            self.__width = value
            self.__height = value

    def update(self, *args, **kwargs):
        '''Update with args and kwargs


        Args:
            (id) 1st-attribute.
            (size) 2nd-attribute.
            (x) 3nd-attribute.
            (y) 4nd-attribute.

        '''
        if args is not None and len(args) != 0:
            if len(args) >= 1:
                if not isinstance(value, int) and args[0] is not None:
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
                    if not isinstance(value, int) and value is not None:
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
