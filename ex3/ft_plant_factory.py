class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def ft_plant_factory(self):
        print(f"Created: {self.name}: {self.height}cm, {self.age} days old")


if __name__ == "__main__":
        rose = Plant("Rose", 25.0, 30)
        oak = Plant("Oak", 200.0, 365)
        cactus = Plant("Cactus", 5.0, 90)
        sunflower = Plant("Sunflower", 80.0, 45)
        fern = Plant("Fern", 15.0, 120)
        print("=== Plant Factory Output ===")
        rose.ft_plant_factory()
        oak.ft_plant_factory()
        cactus.ft_plant_factory()
        sunflower.ft_plant_factory()
        fern.ft_plant_factory()