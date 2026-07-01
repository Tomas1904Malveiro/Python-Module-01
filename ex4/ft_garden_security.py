class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def set_height(self, heigth):
        if heigth < 0:
            print(f"{self.name}: Error, height can't be negative")
            return False
        self.height = float(heigth)
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
        print(f"Plant created {self.name}: {self.height}cm,"
              f"{self.age} days old")


if __name__ == "__main__":
    print("=== Garden Security System ===")
    rose = Plant("Rose", 15.0, 10)
    rose.show()
    print("")
    if rose.set_height(25):
        print("Height updated: 25cm")

    if rose.set_age(30):
        print("Age updated: 30 days")
    print("")
    if not rose.set_height(-5):
        print("Height update rejected")

    if not rose.set_age(-5):
        print("Age update rejected")
    print("")
    print(f"Current state: {rose.name}: {rose.height}cm, {rose.age} days old")
