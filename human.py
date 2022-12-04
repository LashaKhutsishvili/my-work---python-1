from animal import Animal


class Human(Animal):

    def communicate(self):
        return "I am human, so I can talk"

    def can_fly(self):
        return False

    def to_string(self):
        information = {
            "Name": self.name,
            "age": self.age,
            "leg_count": self.leg_count
        }
        return information

