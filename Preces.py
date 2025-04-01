class preces:
    def __init__(self, nosaukums, skaits, cena):
        self.nosaukums = nosaukums
        self.skaits = skaits
        self.cena = cena

    def izvade(self):
        global b_cena
        b_cena = (self.skaits * self.cena)
        return (
            "{} {} cena ir {} eiro, bet 1 {} cena ir {}").format(self.skaits, self.nosaukums, b_cena, self.nosaukums, self.cena)
        
    def cenaArPVN(self):
        global a_cena
        global c_cena
        a_cena = (self.cena*self.skaits) + (self.cena * 0.21)
        c_cena = self.cena + self.cena * 0.21
        return("{} cena ar PVN ir {} eiro, bet 1 {} cena ar PVN ir {}").format(self.nosaukums,a_cena,self.nosaukums,c_cena)

            
prece = preces ("Datora", 3, 500)
prece.izvade()
print(prece.izvade())

print(str(prece.cenaArPVN()))