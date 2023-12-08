#!/usr/bin/python3
class Student:
	"""
	Represents a student.
	"""

	def __init__(self, first_name, last_name, age):


		"""
		Initializes a new Student object.

		Args:
			first_name (str): The first name of the student.
			last_name (str): The last name of the student.
			age (int): The age of the student.
		"""
		self.first_name = first_name
		self.last_name = last_name
		self.age = age


	def to_json(self, attrs=None):


		"""
		Retrieves a dictionary representation of the Student instance.

		Args:
			attrs (list, optional): A list of attribute names to include in the dictionary.
				If None, all attributes are included.
		Returns:
			dict: A dictionary representation of the Student instance.
		"""
		result = {}
		for key, value in self.__dict__.items():
			if attrs is None or key in attrs:
				result[key] = value
		return result
