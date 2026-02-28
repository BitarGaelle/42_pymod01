#!/usr/bin/env python3
class SecurePlant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.__height = height
        self.__age = age

    def set_height(self, new_height: int) -> None:
        if (new_height > 0):
            self.__height = new_height
            print(f"Height updated: {self.__height}cm [OK]")
        else:
            print(f"\nInvalid operation attempted: height \
{new_height}cm [REJECTED]")
            print("Security: Negative height rejected")

    def set_age(self, new_age: int) -> None:
        if (new_age > 0):
            self.__age = new_age
            print(f"Age updated: {self.__age} days [OK]")
        else:
            print(f"\nInvalid operation attempted: age \
{new_age} days [REJECTED]")
            print("Security: Negative age rejected")

    def get_height(self) -> int:
        return self.__height

    def get_age(self) -> int:
        return self.__age

    def display(self) -> None:
        print(f"Plant created: {self.name}")


def ft_garden_security():
    print("=== Garden Security System ===")
    plant = SecurePlant("Rose", 10, 23)
    plant.display()
    plant.set_height(25)
    plant.set_age(30)
    plant.set_height(-5)
    print(f"\nCurrent plant: {plant.name} \
({plant.get_height()}cm, {plant.get_age()} days)")


if __name__ == "__main__":
    ft_garden_security()
