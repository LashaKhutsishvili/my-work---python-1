from human import Human
from cat import Cat
from dog import Dog
from seagull import Seagull

human1 = Human("lasha", 27, 2)
cat1 = Cat("kata", 3, 4)
dog1 = Dog("dzagli", 4, 4)
seagull1 = Seagull("tolia", 1, 2)

print(human1.to_string())
print(human1.can_fly())
print(human1.communicate())

