#!/usr/bin/env python3
class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.__height = height
        self.__age = age

    def display(self) -> None:
        print(f"{self.name}: {self.__height}cm, {self.__age} days old")


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str):
        super().__init__(name, height, age)
        self.__color = color

    def display(self):
        print(f"\n{self.name} (Flower): {self.__height}cm, \
{self.__age} days, {self.__color} color")

    def bloom(self):
        print(f"{self.name} is blooming beautifully!")


class Tree(Plant):
    def __init__(self, name: str, height: int, age: int, diameter: int):
        super().__init__(name, height, age)
        self.__diameter = diameter

    def display(self):
        print(f"\n{self.name} (Tree): {self.__height}cm, {self.__age} days, \
{self.__diameter}cm diameter")

    def produce_shade(self, diameter):
        print(f"{self.name} provides 78 square meters of shade")


class Vegetable(Plant):
    def __init__(self, name: str, height: int, age: int,
                 harvest_season: str, nutritional_value: str):
        super().__init__(name, height, age)
        self.__harvest_season = harvest_season
        self.__nutritional_value = nutritional_value

    def display(self):
        print(f"\n{self.name} (Vegetable): {self.__height}cm, \
{self.__age} days, {self.__harvest_season} harvest")

    def Vegdisplay(self):
        print(f"{self.name} is rich in vitamin {self.__nutritional_value}")


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
