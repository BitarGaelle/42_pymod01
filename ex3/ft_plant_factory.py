#!/usr/bin/env python3
class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def display(self) -> None:
        print(f"Created: {self.name} ({self.height}cm, {self.age} days)")


def ft_plant_factory():
    print("=== Plant Factory Output ===")
    data = [
        ("Rose", 25, 30),
        ("Oak", 200, 365),
        ("Cactus", 5, 90),
        ("Sunflower", 80, 45),
        ("Fern", 15, 120)
    ]
    plants = []
    i = 0
    for name, height, age in data:
        plant = Plant(name, height, age)
        plants.append(plant)
        i += 1
        plant.display()
    print(f"\nTotal plants created: {i}")


if __name__ == "__main__":
    ft_plant_factory()
