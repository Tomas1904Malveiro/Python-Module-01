class Plant:
    class Stats:
        def __init__(self):
            self.grow_count = 0
            self.age_count = 0
            self.show_count = 0

        def record_grow(self):
            self.grow_count = self.grow_count + 1

        def record_age(self):
            self.age_count = self.age_count + 1

        def record_show(self):
            self.show_count = self.show_count + 1

        def display(self):
            print(f"Stats: {self.grow_count} grow, "
                  f"{self.age_count} age, {self.show_count} show")

    def __init__(self, name, height, age):
        self.name = name
        self.height = 0.0
        self.age = 0
        self.growth_rate = 0.8
        self.stats = Plant.Stats()
        self.set_height(height)
        self.set_age(age)

    def show(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old")
        self.stats.record_show()

    def show_stats(self):
        self.stats.display()

    def get_height(self):
        return self.height

    def get_age(self):
        return self.age

    def set_height(self, height):
        if height < 0:
            print(f"{self.name}: Error, height can't be negative")
            return False
        self.height = float(height)
        return True

    def set_age(self, age):
        if age < 0:
            print(f"{self.name}: Error, age can't be negative")
            return False
        self.age = age
        return True

    def grow(self):
        self.set_height(round(self.height + self.growth_rate, 1))
        self.stats.record_grow()

    def update_age(self, days=1):
        self.set_age(self.age + days)
        self.stats.record_age()

    @staticmethod
    def is_older_than_year(age):
        return age > 365

    @classmethod
    def create_anonymous(cls):
        return cls("Unknown plant", 0.0, 0)


class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color
        self.bloomed = False

    def bloom(self):
        self.bloomed = True

    def show(self):
        super().show()
        print(f" Color: {self.color}")
        if self.bloomed:
            print(f" {self.name} is blooming beautifully!")
        else:
            print(f" {self.name} has not bloomed yet")


class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
        self.shade_count = 0

    def produce_shade(self):
        print(f"Tree {self.name} now produces a shade of "
              f"{self.height}cm long and {self.trunk_diameter}cm wide.")
        self.shade_count = self.shade_count + 1

    def show(self):
        super().show()
        print(f" Trunk diameter: {self.trunk_diameter}cm")

    def show_stats(self):
        super().show_stats()
        print(f" {self.shade_count} shade")


class Vegetable(Plant):
    def __init__(self, name, height, age, harvest_season):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = 0

    def update_age(self, days=1):
        super().update_age(days)
        self.nutritional_value = self.nutritional_value + 1

    def show(self):
        super().show()
        print(f" Harvest season: {self.harvest_season}")
        print(f" Nutritional value: {self.nutritional_value}")


class Seed(Flower):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age, color)
        self.seeds = 0

    def bloom(self):
        super().bloom()
        self.seeds = 42

    def show(self):
        super().show()
        print(f" Seeds: {self.seeds}")


def display_stats(plant):
    print(f"[statistics for {plant.name}]")
    plant.show_stats()


if __name__ == "__main__":
    print("=== Garden statistics ===")

    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.is_older_than_year(30)}")
    print(f"Is 400 days more than a year? -> {Plant.is_older_than_year(400)}")
    print("")
    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.growth_rate = 8.0
    rose.show()
    display_stats(rose)
    print("[asking the rose to grow and bloom]")
    rose.grow()
    rose.bloom()
    rose.show()
    display_stats(rose)
    print("")
    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    display_stats(oak)
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    display_stats(oak)
    print("")
    print("=== Seed")
    sunflower = Seed("Sunflower", 80.0, 45, "yellow")
    sunflower.growth_rate = 30.0
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.grow()
    sunflower.update_age(20)
    sunflower.bloom()
    sunflower.show()
    display_stats(sunflower)
    print("")
    print("=== Anonymous")
    unknown = Plant.create_anonymous()
    unknown.show()
    display_stats(unknown)
