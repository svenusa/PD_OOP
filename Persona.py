class persona:
    def __init__(self, vards,idnumber):
        self.vards = vards
        self.idnumber = idnumber

    def izvade(self):
        return (
            "Vards:{}\nID numurs:{}").format(self.vards, self.idnumber)
        

class darbinieks:
    def __init__(self, Alga, Amats):
        self.Alga = Alga
        self.Amats = Amats

    def izvade1(self):
        return (
            "Amats:{}\nAlga:{} eiro").format(self.Amats, self.Alga)
    
Objekts = persona ("Pēteris", "6846342875")
Objekts.izvade()
print(Objekts.izvade())
Objekts1 = darbinieks("2500", "policists")
Objekts1.izvade1()
print(Objekts1.izvade1())

        
