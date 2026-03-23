class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self._height = height
        self._age = age

    def set_height(self, new_height: float) -> None:
        if (new_height > 0):
            self._height = new_height
            print(f"\nHeight updated: {self._height}cm")
        else:
            print(f"\n{self.name}: Error, height can't be negative")
            print("Height update rejected")

    def set_age(self, new_age: int) -> None:
        if (new_age > 0):
            self._age = new_age
            print(f"Age updated: {self._age} days")
        else:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def show(self) -> None:
        print(f"Plant created: {self.name}: {self._height}cm, \
{self._age} days old")


def ft_garden_security():
    print("=== Garden Security System ===")
    plant = Plant("Rose", 15.0, 10)
    plant.show()
    plant.set_height(25.0)
    plant.set_age(30)
    plant.set_height(-5.0)
    plant.set_age(-3)
    print(f"\nCurrent state: {plant.name}: \
{plant.get_height()}cm, {plant.get_age()} days old")


if __name__ == "__main__":
    ft_garden_security()
