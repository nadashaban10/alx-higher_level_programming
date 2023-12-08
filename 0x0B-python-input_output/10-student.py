#!/usr/bin/python3
class Student:
    """Represents a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get a dictionary representation of the student."""
        if not attrs:
            return self.__dict__
        return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
