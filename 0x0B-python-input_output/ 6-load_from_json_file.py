#!/usr/bin/python3
import json


def load_from_json_file(filename):
    """
  Reads a JSON file and creates an object from its content.

  Args:
    filename: The path to the JSON file.

  Returns:
    A Python object representing the decoded JSON data.

    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
