class Plant:
    def __init__(self, name: str, height: float, day: int) -> None:
        self.name = name
        self.height = height
        self.day = day

    def grow(self) -> None:
        self.height += 0.8

    def age(self) -> None:
        self.day += 1

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self.day} days old")


def ft_plant_growth():
    plant = Plant("Rose", 25.0, 30)
    print("=== Garden Plant Growth ===")
    growth = 0.0
    for i in range(1, 8):
        print(f"=== Day {i} ===")
        plant.show()
        plant.grow()
        plant.age()
        growth += 0.8
    print(f"Growth this week : {growth}cm")


if __name__ == "__main__":
    ft_plant_growth()
