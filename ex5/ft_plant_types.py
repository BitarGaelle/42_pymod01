class Plant:
    def __init__(self, name: str, height: float, day: int):
        self.name = name
        self.height = height
        self.day = day

    def grow(self, added_height: float) -> None:
        self.height += added_height

    def age(self, added_age: int) -> None:
        self.day += added_age

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self.day} days old")


class Flower(Plant):
    def __init__(self, name: str, height: float, day: int, color: str):
        super().__init__(name, height, day)
        self.color = color

    def show(self):
        super().show()
        print(f" Color: {self.color}")

    def bloom(self):
        print(f" {self.name} is blooming beautifully!")

    def grow(self, added_height: float) -> None:
        super().grow(added_height)

    def age(self, added_age: int) -> None:
        super().age(added_age)


class Tree(Plant):
    def __init__(self, name: str, height: float, day: int,
                 trunk_diameter: float):
        super().__init__(name, height, day)
        self.trunk_diameter = trunk_diameter

    def show(self):
        super().show()
        print(f" Trunk diameter: {self.trunk_diameter}cm")

    def produce_shade(self):
        print(f"{self.name}  now produces a shade of \
{self.height}cm long and {self.trunk_diameter}cm wide")

    def grow(self, added_height: float) -> None:
        super().grow(added_height)

    def age(self, added_age: int) -> None:
        super().age(added_age)


class Vegetable(Plant):
    def __init__(self, name: str, height: float, day: int,
                 harvest_season: str):
        super().__init__(name, height, day)
        self.harvest_season = harvest_season
        self.nutritional_value = 0

    def show(self):
        super().show()
        print(f" Harvest season: {self.harvest_season}")
        print(f" Nutritional value: {self.nutritional_value}")

    def grow(self, added_height: float) -> None:
        super().grow(added_height)

    def age(self, added_age: int) -> None:
        super().age(added_age)
        self.nutritional_value += 1


def ft_plant_types():
    print("=== Garden Plant Types ===")
    rose = Flower("Rose", 15.0, 10, "red")
    oak = Tree("Oak", 200.0, 365, 5.0)
    tomato = Vegetable("Tomato", 5.0, 10, "April")
    print("=== Flower")
    rose.show()
    print(f" {rose.name} has not bloomed yet")
    print("[asking the rose to bloom]")
    rose.show()
    rose.bloom()
    print("\n=== Tree")
    oak.show()
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    print("\n=== Vegetable")
    tomato.show()
    print("[make tomato grow and age for 20 days]")
    for i in range(20):
        tomato.age(1)
    tomato.grow(42)
    tomato.show()


if __name__ == "__main__":
    ft_plant_types()
