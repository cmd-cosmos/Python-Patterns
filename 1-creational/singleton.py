# singleton creational pattern implementation
# pylint: skip-file
# type: ignore

# ensure single instance of a class exists at a given time

class RegularControlTower:
    def __init__(self) -> None:
        print("Constructing Control Tower Object...")

# 2 objects with unique ids --> 2 separate instances of the class
t1 = RegularControlTower()
t2 = RegularControlTower()

print("t1 id: ", id(t1))
print("t2 id: ", id(t2))
print(t1 is t2)  # False --> as both objs have different ids
