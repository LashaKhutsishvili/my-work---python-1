from animal import Animal


class Cat(Animal):
    def communicate(self):
        return "I am cat, so I can meow"

    def can_fly(self):
        return False

    def to_string(self):
        information = {
            "Name": self.name,
            "age": self.age,
            "leg_count": self.leg_count
        }
        return information