#!/usr/bin/env python3
"""
we define a class called plant where we have the constuctor,the grow method
the age method and the get_info for printing that plant informations
"""


class Plant:
    def __init__(self, name: str, height: int, daysold: int):
        self.name = name
        self.height = height
        self.daysold = daysold

    def grow(self):
        self.height += 6

    def age(self):
        self.daysold += 7

    def get_info(self):
        print(f"Created:{self.name} ({self.height}cm,"
              f"{self.daysold} days old)")


"""
in this exercise we try to create plant in a more simple way
we declare a list of plants information, a simple for loop
can go over the list and create for each plant in it the object
and we store that inside a garden list with all the plants
"""

plants = [
    ["Rose", 25, 30],
    ["Oak", 200, 365],
    ["Cactus", 5, 90],
    ["Sunflower", 80, 45],
    ["Fern", 15, 120]
]

garden = []

garden = [Plant(*plant) for plant in plants]
print("=== Plant Factory Output ===")
plants_created = 0
"""
a simple loop to print the output of each plant inside the list
plants_created is a varriable that stores the number of plants created
"""
for plant in garden:
    plant.get_info()
    plants_created += 1
print(f"\nTotal plants created:{plants_created}")
