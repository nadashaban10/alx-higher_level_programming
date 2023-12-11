#!/usr/bin/python3
'''class square (rectanagle) inherits'''
from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    '''repressention square'''

    def __init__(self, size, x=0, y=0, id=None):
        '''
        Initialize a new square object.

        Args:
            size: The side length of the square.
            x: The X of the square.
            y: The Y of the square.
            id: ID of the square.
        '''

        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''
            string representation of the square
            Returns:
            A string of the format "[Square] (<id>) <x>/<y> - <size>".
        '''
        return f"[square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """
        Retrieves the size attribute
        """
        return self.Width

    @size.setter
    def size(self, value):
        '''if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")'''
        self.__width = value
        self.__height = value

    def update(self, *args, **kwargs):
        """Update the Square.

        Args:
            *args (ints): New attribute values.
                - 1st argument represents id attribute
                - 2nd argument represents size attribute
                - 3rd argument represents x attribute
                - 4th argument represents y attribute
            **kwargs (dict): New key/value pairs of attributes.
        """
        if args is not None and len(args) != 0:
            if len(args) >= 1:
                if not isinstance(args[0], int) and args[0] is not None:
                    raise TypeError("id must be an integer")
                self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    if not isinstance(value, int) and value is not None:
                        raise TypeError("id must be an integer")
                    self.id = value
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """
    Return the dictionary representation of a Rectangle.

    Returns:
        dict: A dictionary containing the attributes of the Rectangle.
        """
        return {
            "id": self.id,
            "x": self.x,
            "size": self.width,
            "y": self.y,
        }
