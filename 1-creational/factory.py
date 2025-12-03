#pylint: skip-file
#type: ignore

# factory: separate creation from use

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

if __name__ == "__main__":
    main()