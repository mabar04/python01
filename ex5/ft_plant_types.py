#!/usr/bin/env python3
"""
This exercise demonstrates basic Object-Oriented Programming
concepts in Python,including inheritance, attribute extension,
and method specialization.

A base class `Plant` defines shared attributes for all plant-related objects.
Child classes (`Flower`, `Tree`, and `Vegetable`) inherit these attributes
while adding their own unique properties and behaviors.

- `Flower` adds a color attribute and a bloom action.
- `Tree` adds a trunk diameter attribute and can provide shade.
- `Vegetable` adds information about harvest season and nutritional value.

The goal of this exercise is to show how inheritance reduces repeated code and
allows specialized classes to extend common functionality while sharing the
same base structure.
"""


class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str):
        super().__init__(name, height, age)
        self.color = color

    def bloom(self):
        print(f"{self.name} is blooming beautifully!")


class Tree(Plant):
    def __init__(self, name: str, height: int, age: int, trunk_diameter: int):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
        print("Oak provides 78 square meters of shade")


class Vegetable(Plant):
    def __init__(self, name: str, height: int, age: int,
                 harvest_season: str, nutritional_value: str):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value


print("=== Garden Plant Types ===\n")
flower1 = Flower("Rose", 25, 30, "red")
flower2 = Flower("Tulip", 20, 50, "purple")
tree1 = Tree("Oak", 500, 1825, 50)
tree2 = Tree("Maple", 300, 1500, 60)
vegetable1 = Vegetable("Tomato", 80, 90, "summer harvest", "C")
vegetable2 = Vegetable("Carrot", 70, 80, "winter harvest", "A")
print(f"{flower1.name} (Flower): {flower1.height}cm, {flower1.age} days,"
      f"{flower1.color} color")
flower1.bloom()
print("\n")
print(f"{tree1.name} (Tree): {tree1.height}cm, {tree1.age} days,"
      f" {tree1.trunk_diameter}cm diameter")

tree1.produce_shade()

print("\n")
print(f"{vegetable1.name} (Vegetable): {vegetable1.height}cm,"
      f"{vegetable1.age} days, {vegetable1.harvest_season}")
print(f"{vegetable1.name} is rich in vitamin {vegetable1.nutritional_value}")
