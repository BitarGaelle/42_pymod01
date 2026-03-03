#!/usr/bin/env python3
# instance methods, the usual methods, where you call them on an instance.
# (u create an instance and call the method)
###
# class methods, (@classmethod) take cls as the first parameter,
# tied to the class not the instance
# and access class-level data not instance-lvl data
# static methods, (@staticmethod) doesnt take cls, self,
# it's a fnct inside the class for organization purposes
# cannot access instance or class attributes unless passed explicitly

class Plant:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height
        self.plant_type = "regular"

    def grow(self):
        self.height += 1
        return f"{self.name} grew 1cm"

    def display(self):
        return f"- {self.name}: {self.height}cm"


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, color: str):
        super().__init__(name, height)
        self.color = color
        self.blooming = False
        self.plant_type = "flowering"

    def grow(self):
        self.blooming = True
        return (super().grow())

    def display(self):
        s = super().display()
        if (self.blooming is False):
            return f"{s}, {self.color} flowers"
        else:
            return f"{s}, {self.color} flowers (blooming)"


class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, height: int, color: str, points: int):
        super().__init__(name, height, color)
        self.points = points
        self.plant_type = "prize flowers"

    def display(self):
        s = super().display()
        return f"{s}, Prize points: {self.points}"


class Garden:
    def __init__(self, name: str):
        self.name = name
        self.plants = []

    def add_plant(self, plant: Plant):
        self.plants.append(plant)
        print(f"Added {plant.name} to {self.name}'s garden")

    def grow_all(self):
        print(f"\n{self.name} is helping all plants grow...")
        for plant in self.plants:
            print(plant.grow())

    def report(self):
        print(f"\n=== {self.name}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.plants:
            print(f"{plant.display()}")
        print()


class GardenManager:
    gardens = []

    def __init__(self, name: str):
        self.name = name

    @classmethod
    def create_garden_network(cls, garden: Garden):
        cls.gardens.append(garden)

    class GardenStats:

        @staticmethod
        def total_growth_plants(garden: Garden):
            total_growth = 0
            total_plants = 0
            for plant in garden.plants:
                total_plants += 1
                total_growth += 1
            print(f"Plants added: {total_plants}, \
Total growth: {total_growth}cm")

        @staticmethod
        def total_plant_types(garden: Garden):
            regular = 0
            flowering = 0
            prize = 0
            for plant in garden.plants:
                if plant.plant_type == "regular":
                    regular += 1
                elif plant.plant_type == "flowering":
                    flowering += 1
                elif plant.plant_type == "prize flowers":
                    prize += 1
            print(f"Plant types: {regular} regular, \
{flowering} flowering, {prize} prize flowers\n")

        @staticmethod
        def is_valid(height: int):
            if height <= 0:
                print("Height validation test: False")
            else:
                print("Height validation test: True")

        @classmethod
        def garden_score(cls):
            res = ""
            for i in GardenManager.gardens:
                garden_score = 0
                for plant in i.plants:
                    if (plant.plant_type == "prize flowers"):
                        garden_score += plant.points
                res += f"{i.name}: {garden_score}, "
            print("Garden scores - " + res[:-2])

        @classmethod
        def garden_total(cls):
            garden_count = 0
            for garden in GardenManager.gardens:
                garden_count += 1
            print(f"Total gardens managed: {garden_count}")


def ft_garden_analytics():
    print("=== Garden Management System Demo ===\n")
    plants1 = [
        Plant("Oak Tree", 100),
        FloweringPlant("Rose", 25, "red"),
        PrizeFlower("Sunflower", 50, "yellow", 10),
        # PrizeFlower("Tulip", 16, "pink", 30),
        # PrizeFlower("Jasmin", 50, "white", 15)
    ]

    plants2 = [
        Plant("Palm Tree", 196),
        FloweringPlant("Lavendar", 33, "purple"),
        PrizeFlower("Cactus", 70, "green", 20)
    ]

    g1 = Garden("Alice")
    g2 = Garden("Bob")
    GM = GardenManager

    for plant in plants1:
        g1.add_plant(plant)
    g1.grow_all()
    g1.report()

    for plant in plants2:
        g2.add_plant(plant)
    # g2.grow_all()
    # g2.report()

    GM.create_garden_network(g1)
    GM.create_garden_network(g2)
    GM.GardenStats.total_growth_plants(g1)
    GM.GardenStats.total_plant_types(g1)
    GM.GardenStats.is_valid(plants1[0].height)
    GM.GardenStats.garden_score()
    GM.GardenStats.garden_total()


if __name__ == "__main__":
    ft_garden_analytics()
