#!/usr/bin/env python3
"""
This exercise demonstrates an advanced Garden Management System built with
Object-Oriented Programming concepts in Python.

Main OOP concepts used:
- Encapsulation: Sensitive attributes in `GardenManager` and `Garden` are
  protected through name mangling and accessed via methods rather than direct
  manipulation.
- Inheritance: `FloweringPlant` extends `Plant` and `PrizeFlower` further
  specializes flowering behavior by adding prize points.
- Composition: A Garden contains multiple Plant objects, and a GardenManager
  manages multiple Garden objects.
- Nested Classes: `GardenManager.GardenStats` provides analytical and reporting
  utilities for the manager without exposing internal state.
- Class methods and static methods: Used for utility behavior and alternative
  object creation (`create_garden_network`).
- Polymorphism: Overriding `get_info()` methods allows different plant types to
  print customized details while sharing the same interface.

Program behavior:
A GardenManager can manage multiple gardens, grow plants, and generate reports.
The system simulates adding plants, tracking growth, counting plant types,
validating data, and producing formatted output for a selected garden.
This exercise highlights how abstraction and hierarchy help organize features,
reuse code, and keep data protected.
"""

"""
a class for the garden manager who take cares for the gardens of multiple
owners where we can add a garden or remove it and get stats about the gardens
"""


class GardenManager:
    def __init__(self, name: str):
        self.__name = name
        self.__gardens: list = []

    def grow_all(self, owner: str):
        for garden in self.__gardens:
            if garden.get_owner() == owner:
                garden.grow_all()
                print()

    def add_garden(self, garden):
        self.__gardens += [garden]

    def remove_garden(self, garden):
        self.__gardens = [g for g in self.__gardens if g != garden]

    def garden_managed(self):
        i = 0
        for garden in self.__gardens:
            i = i + 1
        print(f"Total gardens managed: {i}")

    def get_garden_score(self):
        print("Garden scores - ", end="")
        for garden in self.__gardens:
            print(f"{garden.get_owner()}: {garden.score}", end="")
            if (garden.get_owner() == "Alice"):
                print(", ", end="")
        print()

    @classmethod
    def create_garden_network(cls, owners: list):
        return [cls(owner) for owner in owners]

    class GardenStats:
        @staticmethod
        def total_plants(manager):
            total = 0
            for garden in manager.__gardens:
                total += garden.count_plants
            return total
        """
        Prints a detailed report for all gardens owned by a given owner.
        The report includes:
        - A header with the owner's name
        - A list of all plants in the owner's gardens (via plant.get_info())
        - Total number of plants added
        - Total growth in centimeters
        - A breakdown of plant types: regular, flowering, and prize flowers
        - A height validation test that checks if any plant has a negative
          height
        Output
        ------
        This method prints formatted information to stdout and does not return
        a value.
        """
        @staticmethod
        def garden_report(manager, owner: str):
            print(f"=== {owner}'s Garden Report ===")
            print("Plants in garden:")
            for garden in manager._GardenManager__gardens:
                if garden.get_owner() == owner:
                    for plant in garden.get_plants():
                        plant.get_info()
                    print()
                    print(f"Plants added : {garden.count_plants()},"
                          f" Total growth: {garden.total_growth}cm")
                    print("Plant types: ", end="")
                    regular = garden.count_by_type("regular")
                    print(f"{regular} regular,", end="")
                    flowering = garden.count_by_type("flowering")
                    print(f"{flowering} flowering,", end="")
                    prizeflowers = garden.count_by_type("prize flowers")
                    print(f"{prizeflowers} prize flowers", end="")
                    print("\n")
                    validation = 1
                    for plant in garden.get_plants():
                        if (plant.height < 0):
                            validation = -1
                    if validation == 1:
                        print("Height validation test: True")
                    else:
                        print("Height validation test: False")


class Garden:
    """
    Represents a garden owned by a specific person, containing multiple plants
    and tracking statistics such as total growth and score.

    Each Garden instance maintains:
      - The garden owner (private)
      - A list of plant objects
      - A cumulative growth counter
      - A score value used for comparison or evaluation

    Parameters
    ----------
    owner : str
        The name of the garden owner.
    score : int
        Initial score for the garden, used for reporting or ranking.

    Attributes
    ----------
    _Garden__owner : str
        The private name of the garden owner.
    _Garden__plants : list
        A list of plant objects currently in the garden.
    total_growth : int
        Accumulated growth from all plants (increments during grow_all()).
    score : int
        Score assigned to the garden.

    Methods
    -------
    add_plant(plant)
        Adds a plant to the garden and prints a confirmation message.
    remove_plant(plant)
        Removes a plant from the garden if present.
    grow_all()
        Instructs all plants to grow and increments the total growth count.
    count_plants()
        Returns the total number of plants in the garden.
    count_by_type(type)
        Counts the number of plants of a given type.
    get_owner()
        Returns the name of the garden owner.
    get_plants()
        Returns the list of plant objects stored in the garden.

    Notes
    -----
    - This class does not enforce plant type or structure; plants are assumed
      to have `.grow()`, `.name`, `.plant_type` attributes for compatibility.
    """
    def __init__(self, owner: str, score: int):
        self.__owner = owner
        self.__plants = []
        self.total_growth = 0
        self.score = score

    def add_plant(self, plant):
        self.__plants += [plant]
        print(f"Added {plant.name} to {self.__owner}'s garden")

    def remove_plant(self, plant):
        self.__plants = [p for p in self.__plants if p != plant]

    def grow_all(self):
        print(f"{self.__owner} is helping all plants grow...")
        for plant in self.__plants:
            plant.grow()
            self.total_growth += 1

    def count_plants(self):
        i = 0
        for plant in self.__plants:
            i += 1
        return i

    def count_by_type(self, type):
        i = 0
        for plant in self.__plants:
            if plant.plant_type == type:
                i += 1
        return i

    def get_owner(self):
        return self.__owner

    def get_plants(self):
        return self.__plants


class Plant:
    def __init__(self, name, height, daysold):
        self.name = name
        self.height = height
        self.daysold = daysold
        self.plant_type = "regular"

    def grow(self):
        print(f"{self.name} grew 1 cm")
        self.height += 1

    def get_info(self):
        print(f"- {self.name}: {self.height}cm")


class FloweringPlant(Plant):
    def __init__(self, name, height, daysold, color):
        super().__init__(name, height, daysold)
        self.color = color
        self.status = "blooming"
        self.plant_type = "flowering"

    def get_info(self):
        print(f"- {self.name}: {self.height}cm, {self.color} flowers "
              f"({self.status})")


class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, daysold, color):
        super().__init__(name, height, daysold, color)
        self.plant_type = "prize flowers"
        self.Prize_points = 10

    def get_info(self):
        print(f"- {self.name}: {self.height}cm, {self.color} flowers "
              f"({self.status}), "
              f"Prize points: {self.Prize_points}")


print("=== Garden Management System Demo ===\n")
manager1 = GardenManager("kevin")
garden1 = Garden("Alice", 218)
garden2 = Garden("Bob", 92)
manager1.add_garden(garden1)
manager1.add_garden(garden2)
plant1 = Plant("Oak Tree", 100, 30)
plant2 = FloweringPlant("Rose", 25, 20, "red")
plant3 = PrizeFlower("Sunflower", 50, 40, "yellow")
garden1.add_plant(plant1)
garden1.add_plant(plant2)
garden1.add_plant(plant3)
print()
manager1.grow_all("Alice")
GardenManager.GardenStats.garden_report(manager1, "Alice")
manager1.get_garden_score()
manager1.garden_managed()
