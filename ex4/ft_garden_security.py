#!/usr/bin/env python3
"""
In this exercise, we manage private data using encapsulation.
Encapsulation means protecting data from direct access or modification
that could harm the system.

_: indicates that the attribute is protected. It can be accessed, but
   it is intended for internal use within the class or its subclasses.

__: indicates that the attribute is private. It cannot be accessed
    directly from outside the class, only through methods defined inside.
"""


class SecurePlant:
    def __init__(self, name: str, height: int, daysold: int):
        self.name = name
        self.__height = height
        self.__daysold = daysold
        print(f"Plant created: {self.name}")
    """
    in these methods,we can set the conditions that we want for protecting
    the data from corruption
    """
    def set_height(self, height):
        if height < 0:
            print(f"Invalid operation attempted: height {height}cm [Rejected]")
            print("Security: Negative height rejected")
            return
        self.__height = height
        print(f"Height updated: {self.__height}cm [OK]")

    def set_age(self, age):
        if age < 0:
            print(f"Invalid operation attempted: age {age}days [Rejected]")
            print("Security: Negative age rejected")
            return
        self.__daysold = age
        print(f"age updated: {self.__daysold} days [OK]")
    """
    in these methods,we can get the informations that we want like age
    and height
    """
    def get_height(self):
        return self.__height

    def get_age(self):
        return self.__daysold


print("=== Garden Security System ===")
plant1 = SecurePlant("Rose", 15, 10)
plant1.set_height(25)
plant1.set_age(30)
print("\n")
plant1.set_height(-5)
print("\n")
print(f"Current plant: {plant1.name} ({plant1.get_height()}cm "
      f"{plant1.get_age()} days)")
