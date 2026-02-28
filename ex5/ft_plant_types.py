#!/usr/bin/env python3
class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age

    def display(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str):
        super().__init__(name, height, age)
        self.color = color

    def display(self):
        print(f"\n{self.name} (Flower): {self.height}cm, \
{self.age} days, {self.color} color")

    def bloom(self):
        print(f"{self.name} is blooming beautifully!")


class Tree(Plant):
    def __init__(self, name: str, height: int, age: int, diameter: int):
        super().__init__(name, height, age)
        self.diameter = diameter

    def display(self):
        print(f"\n{self.name} (Tree): {self.height}cm, {self.age} days, \
{self.diameter}cm diameter")

    def produce_shade(self, diameter):
        print(f"{self.name} provides 78 square meters of shade")


class Vegetable(Plant):
    def __init__(self, name: str, height: int, age: int,
                 harvest_season: str, nutritional_value: str):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def display(self):
        print(f"\n{self.name} (Vegetable): {self.height}cm, \
{self.age} days, {self.harvest_season} harvest")

    def Vegdisplay(self):
        print(f"{self.name} is rich in vitamin {self.nutritional_value}")


def ft_plant_types():
    print("=== Garden Plant Types ===")
    rose = Flower("Rose", 25, 30, "red")
    oak = Tree("Oak", 500, 1825, 50)
    tomato = Vegetable("Tomato", 80, 90, "summer", "C")
    rose.display()
    rose.bloom()
    oak.display()
    oak.produce_shade(50)
    tomato.display()
    tomato.Vegdisplay()


if __name__ == "__main__":
    ft_plant_types()
