#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.daysold = age
    """
    The only difference between this exercise and the previous is that this one
    needs to define a method witch are functions that the class instance work
    with to make a data change or an action
    """
    def grow(self):
        self.height += 6

    def age(self):
        self.daysold += 7

    def get_info(self):
        print(f"{self.name}: {self.height}cm, "
              f"{self.daysold} days old")


"""
we define a plant object and we call it's methods to see if it works properly
getinfo():to get plant informations (age,height)
grow():to grow the plant height
age():to grow the plant age
"""
plant1 = Plant("Rose", 25, 30)
print("=== Day 1 ===")
plant1.get_info()
plant1.grow()
plant1.age()
print("=== Day 7 ===")
plant1.get_info()
print("Growth this week: +6cm")
