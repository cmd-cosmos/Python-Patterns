# singleton creational pattern implementation
# pylint: skip-file
# type: ignore

# ensure single instance of a class exists at a given time
# __init__ --> controls initialization of an instance
# __new__ ---> controls how new instance is created

from typing_extensions import Self


class RegularControlTower:
    def __init__(self) -> None:
        print("Constructing Control Tower Object.")

# 2 objects with unique ids --> 2 separate instances of the class
t1 = RegularControlTower()
t2 = RegularControlTower()

print("t1 id: ", id(t1))
print("t2 id: ", id(t2))
print(t1 is t2)  # False --> as both objs have different ids

print("*"*70)

class SingletonControlTower:
    _instance = None # track any active instance to ensure not more than 1 created
   
    def __new__(cls) -> Self:
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            print("Constructing New Control Tower Object")
        else:
            print("Using previously created object for repeated instance req.")
        return cls._instance
    
    def flightControl(self, flightID):
        print("Controling Flight: ", flightID)
        

st1 = SingletonControlTower()
st2 = SingletonControlTower()

print("st1 id: ", id(st1))
print("st2 id: ", id(st2))
print(st1 is st2)  # True --> as both objs have same ids


st1.flightControl("IN121")
st1.flightControl("IN178")
st2.flightControl("US900")
