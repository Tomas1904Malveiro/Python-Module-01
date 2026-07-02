class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

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

    def get_height(self):
        return self.height

    def get_age(self):
        return self.age

    def show(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old")


if __name__ == "__main__":
    print("=== Garden Security System ===")
    rose = Plant("Rose", 15.0, 10)
    print("Plant created: ", end="")
    rose.show()
    print("")
    if rose.set_height(25):
        print("Height updated: 25cm")

    if rose.set_age(30):
        print("Age updated: 30 days")
    print("")
    if not rose.set_height(-1):
        print("Height update rejected")

    if not rose.set_age(-1):
        print("Age update rejected")
    print("")
    print("Current state: ", end="")
    rose.show()
