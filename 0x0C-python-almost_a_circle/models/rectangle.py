from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size: int, x: int = 0, y: int = 0, id: int = None):
        """
        Initialize a new Square object.

        Args:
            size: The side length of the square.
            x: The X coordinate of the square (default: 0).
            y: The Y coordinate of the square (default: 0).
            id: The optional ID of the square (default: None).
        """
        super().__init__(size, size, x, y, id)

    def __str__(self) -> str:
        """Return a string representation of the square."""
        return f"[Square] ({self.id}) ({self.x})/({self.y}) - {self.width}"

    @property
    def size(self) -> int:
        """Get the size of the square."""
        return self.__width

    @size.setter
    def size(self, value: int):
        """Set the size of the square."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value <= 0:
            raise ValueError("size must be greater than 0")
        self.__width = value
        self.__height = value
