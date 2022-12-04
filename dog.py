from animal import Animal


class Dog(Animal):
    def communicate(self):
        return "I am Dog, so I can bark"

    def can_fly(self):
        return False

    def to_string(self):
        information = {
            "Name": self.name,
            "age": self.age,
            "leg_count": self.leg_count
        }
        return information
