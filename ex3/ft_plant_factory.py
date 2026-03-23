class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        print(f"Created: {self.name}: {self.height:.1f}cm, {self.age} days")


def ft_plant_factory():
    print("=== Plant Factory Output ===")
    data = [
        ("Rose", 25, 30),
        ("Oak", 200, 365),
        ("Cactus", 5, 90),
        ("Sunflower", 80, 45),
        ("Fern", 15, 120)
    ]
    for name, height, age in data:
        plant = Plant(name, height, age)
        plant.show()


if __name__ == "__main__":
    ft_plant_factory()
