#!/usr/bin/env python3
class Plant:
    def __init__(self, name: str, height: int, day: int) -> None:
        self.name = name
        self.height = height
        self.day = day

    def grow(self) -> None:
        self.height += 6

    def age(self) -> None:
        self.day += 6

    def display(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.day} days old")


def get_info() -> None:
    print("Growth this week: +6cm\n")


def ft_plant_growth():
    plants = [
        Plant("Rose", 25, 30),
        Plant("Sunflower", 80, 45),
        Plant("Cactus", 15, 120)
    ]
    print("=== Day 1 ===")
    for plant in plants:
        plant.display()

    print("=== Day 7 ===")
    for plant in plants:
        plant.grow()
        plant.age()
        plant.display()
        get_info()


if __name__ == "__main__":
    ft_plant_growth()
