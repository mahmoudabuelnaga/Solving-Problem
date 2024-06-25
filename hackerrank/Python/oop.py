class Parot:
    # species = "bird"

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def sing(self, song):
        return "{} is {}".format(self.name, song)
    
    def dance(self):
        return "{} is now dancing".format(self.name)
    
blu = Parot("Blu", 10)
woo = Parot("Woo", 15)

print(blu.sing("'Happy'"))
print(blu.dance())