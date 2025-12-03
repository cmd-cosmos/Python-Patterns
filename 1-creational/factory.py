#pylint: skip-file
#type: ignore

# factory: separate creation from use

if 0:
    class Falcon:
        def manufacture(self):
            print("Manufacturing a Falcon-9.")

    class FalconHeavy:
        def manufacture(self):
            print("Manfacturing a Falcon Heavy.")

    class Starship:
        def manufacture(self):
            print("Manfacturing a Starship Superheavy.")

    def main():
        inp = input("what kind of rocket should we manufature: ")

        if inp == "f9":
            f9 = Falcon()
            f9.manufacture()
            return
        elif inp =="fh":
            fh =  FalconHeavy()
            fh.manufacture()
            return
        elif inp == "ss":
            ss = Starship()
            ss.manufacture()
            return
        else:
            print("Invalid Vehicle ID")
            return
#####################################################################################
    
from abc import ABC, abstractmethod

class RocketABC(ABC):
    @abstractmethod
    def manufacture(self):
        pass

class Falcon9(RocketABC):
    def manufacture(self):
        print("Manufacturing a Falcon-9.")
        
class FalconHeavy(RocketABC):
    def manufacture(self):
        print("Manfacturing a Falcon Heavy.")
    
class Starship(RocketABC):
    def manufacture(self):
        print("Manfacturing a Starship Superheavy.")

class RocketFactory:
    id_map = {
        "f9" : Falcon9,
        "fh" : FalconHeavy,
        "ss" : Starship,
    }

    @staticmethod
    def manufacture_rocket(id_inp):
        selected_class = RocketFactory.id_map.get(id_inp.lower())
        if selected_class is None:
            raise ValueError("Invalid Vehicle ID")
        return selected_class()
    
def main():
    inp = input("enter LV id (f9/fh/ss): ")

    try:
        obj = RocketFactory.manufacture_rocket(inp)
        obj.manufacture()
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()