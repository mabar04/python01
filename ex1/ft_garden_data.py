#!/usr/bin/env python3
"""
in this exercise, we create a class called Plant
a class is like a blueprint of how the object will
be created and what they need as a attributes
"""


class Plant:
    """
    Represents a plant in the garden.
    Attributes:
    name (str): Name of the plant
    height (int): Height in cm
    age (int): Age in days
    """

    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age


"""
imolementing the class by creating 3 objects and print
them to the screen
"""
print("=== Garden Plant Registry ===")
plant1 = Plant("Rose", 25, 30)
plant2 = Plant("Sunflower", 80, 45)
plant3 = Plant("Cactus", 15, 120)
print(f"{plant1.name}: {plant1.height}cm, {plant1.age} days old")
print(f"{plant2.name}: {plant2.height}cm, {plant2.age} days old")
print(f"{plant3.name}: {plant3.height}cm, {plant3.age} days old")
