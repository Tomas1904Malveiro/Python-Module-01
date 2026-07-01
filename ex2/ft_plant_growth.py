class Plant:
    def __init__(self, name, height, age, growth):
        self.name = name
        self.height = height
        self.age = age
        self.growth = growth

    def show(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old")

    def grow(self):
        self.height = round(self.height + self.growth, 1)

    def days(self):
        self.age = self.age + 1


if __name__ == "__main__":
    rose = Plant("Rose", 25.0, 30, 0.8)
    print("=== Garden Plant Growth ===")
    rose.show()
    initial_height = rose.height
    for day in range(1, 8):
        rose.grow()
        rose.days()
        print(f"=== Day {day} ===")
        rose.show()
    total_growth = round(rose.height - initial_height, 1)
    print(f"Growth this week: {total_growth}cm")
