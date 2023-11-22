#!/usr/bin/python3
class MagicClass:
    def __init__(self, radius):
        if not isinstance(radius, (int, float)):
            raise TypeError('radius must be a number')

        self._MagicClass__radius = radius

    @property
    def area(self):
        return self._MagicClass__radius ** 2 * math.pi

    @property
    def circumference(self):
        return 2 * math.pi * self._MagicClass__radius
