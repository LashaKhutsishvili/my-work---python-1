from animal import Animal


class Seagull(Animal):
    def communicate(self):
        return "I am seagull, so I can ....."

    def can_fly(self):
        return True

    def to_string(self):
        information = {
            "Name": self.name,
            "age": self.age,
            "leg_count": self.leg_count
        }
        return information
