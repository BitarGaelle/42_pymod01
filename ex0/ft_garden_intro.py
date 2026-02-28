#!/usr/bin/env python3
plant = "rose"
height = 25
age = 30


def ft_garden_intro():
    print("=== Welcome to My Garden ===")
    print("Plant:", plant.capitalize())
    print(f"Height: {height}cm")
    print("Age:", age, "days")
    print()
    print("=== End of Program ===")


if __name__ == "__main__":
    ft_garden_intro()
