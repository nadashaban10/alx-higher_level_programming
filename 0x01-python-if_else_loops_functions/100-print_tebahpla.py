#!/usr/bin/python3
for char in chr(ord('z') + 1)[::-1]:
    print(char.lower() if char.isupper() else char.upper(), end='')
