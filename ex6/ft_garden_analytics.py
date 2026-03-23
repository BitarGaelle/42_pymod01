class Plant:
    class _Stats:
        def __init__(self):
            self.show = 0
            self.grow = 0
            self.age = 0

    def __init__(self, name: str, height: float, day: int):
        self.name = name
        self.height = height
        self.day = day
        self._stats = self._Stats()

    def grow(self, added_height: float) -> None:
        self.height += added_height
        self._stats.grow += 1

    def age(self, added_age: int) -> None:
        self.day += added_age
        self._stats.age += 1

    def show(self) -> None:
        self._stats.show += 1
        print(f"{self.name}: {self.height:.1f}cm, {self.day} days old")

    @staticmethod
    def older_than_year(given_age: int) -> bool:
        if given_age < 365:
            return (False)
        else:
            return (True)

    @classmethod
    def anonymous_plant(cls):
        return cls("Unknown plant", 0.0, 0)


class Flower(Plant):
    def __init__(self, name: str, height: float, day: int, color: str):
        super().__init__(name, height, day)
        self.color = color

    def show(self):
        super().show()
        print(f" Color: {self.color}")

    def bloom(self) -> None:
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
        self._stats.shade = 0

    def show(self):
        super().show()
        print(f" Trunk diameter: {self.trunk_diameter}cm")

    def produce_shade(self):
        self._stats.shade += 1
        print(f"Tree {self.name} now produces a shade of \
{self.height}cm long and {self.trunk_diameter}cm wide.")

    def grow(self, added_height: float) -> None:
        super().grow(added_height)

    def age(self, added_age: int) -> None:
        super().age(added_age)


class Seed(Flower):
    def __init__(self, name: str, height: float, day: int, color: str) -> None:
        super().__init__(name, height, day, color)
        self.seeds = 0

    def bloom(self):
        super().bloom()
        self.seeds = 42

    def show(self):
        super().show()

    def grow(self, added_height: float) -> None:
        super().grow(added_height)

    def age(self, added_age) -> None:
        super().age(added_age)


def display_stats(plant: Plant) -> None:
    print(f"[statistics for {plant.name}]")
    print(f"Stats: {plant._stats.grow} grow, \
{plant._stats.age} age, {plant._stats.show} show")


def ft_garden_analytics():
    print("=== Garden statistics ===")
    rose = Flower("Rose", 15.0, 10, "red")
    oak = Tree("Oak", 200.0, 365, 5.0)
    sunflower = Seed("Sunflower", 80.0, 45, "yellow")
    print("=== Check year-old")
    check_days1 = 30
    check_days2 = 400
    print(f"Is {check_days1} days more than a year? \
-> {Plant.older_than_year(check_days1)}")
    print(f"Is {check_days2} days more than a year? \
-> {Plant.older_than_year(check_days2)}")

    print("\n=== Flower")
    rose.show()
    print(f" {rose.name} has not bloomed yet")
    display_stats(rose)
    print("[asking the rose to grow and bloom]")
    rose.grow(8.0)
    rose.show()
    rose.bloom()
    display_stats(rose)

    print("\n=== Tree")
    oak.show()
    display_stats(oak)
    print(f" {oak._stats.shade} shade")
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    display_stats(oak)
    print(f" {oak._stats.shade} shade")

    print("\n=== Seed")
    sunflower.show()
    print(f" {sunflower.name} has not bloomed yet")
    print(f" Seeds: {sunflower.seeds}")
    print("[make sunflower grow, age and bloom]")
    sunflower.grow(30.0)
    sunflower.age(20)
    sunflower.show()
    sunflower.bloom()
    print(f" Seeds: {sunflower.seeds}")
    display_stats(sunflower)

    print("\n=== Anonymous")
    unknown = Plant.anonymous_plant()
    unknown.show()
    display_stats(unknown)


if __name__ == "__main__":
    ft_garden_analytics()
