import math
class Figura:
    def perimetrs(self):
        pass
    def izvade (self):
        return perimetrs()
    
class kvadrats(Figura):
    def __init__(self, nosaukums, mala1, mala2, mala3, mala4):
     self.nosaukums = nosaukums
     self.mala1 = mala1
     self.mala2 = mala2
     self.mala3 = mala3
     self.mala4 = mala4

    mala1 = input(float("{} 1.malas garumu")).format(self.nosaukums)
    mala2 = input(float("{} 2.malas garumu")).format(self.nosaukums)
    mala3 = input(float("{} 3.malas garumu")).format(self.nosaukums)
    mala4 = input(float("{} 4.malas garumu")).format(self.nosaukums)

    def perimetrs1 (self):
        return self.mala1 + self.mala2 + self.mala3 + self.mala4
    
objekts = kvadrats ("kvadrāta")

class taisnsturis(Figura):
    def __init__(self, nosaukums, mala1, mala2, mala3, mala4):
     self.nosaukums = nosaukums
     self.mala1 = mala1
     self.mala2 = mala2
     self.mala3 = mala3
     self.mala4 = mala4

    def perimetrs2 (self):
        return self.mala1 + self.mala2 + self.mala3 + self.mala4
    
class trijsturis(Figura):
    def __init__(self, nosaukums, mala1, mala2, mala3):
     self.nosaukums = nosaukums
     self.mala1 = mala1
     self.mala2 = mala2
     self.mala3 = mala3
 

    def perimetrs3 (self):
        return self.mala1 + self.mala2 + self.mala3
    
