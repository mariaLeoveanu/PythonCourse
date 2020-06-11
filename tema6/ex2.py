class Catalog:
    objects = []

    def __init__(self, nume, pret, gramaj):
        if not type(pret) == int or not type(gramaj) == int:
            print("Introduceti valori numerice pentru pret si gramaj!")
            return
        self.nume = nume
        self.pret = pret
        self.gramaj = gramaj
        Catalog.objects.append(self)

    @staticmethod
    def afisare_lista():
        return_string = ''
        for prajitura in Catalog.objects:
            return_string += str(prajitura) + "\n"
        return return_string

    @staticmethod
    def sortare_gramaj():
        Catalog.objects.sort(key=lambda x: x.gramaj)
        return Catalog.afisare_lista()

    @staticmethod
    def sortare_pret():
        Catalog.objects.sort(key=lambda x: x.pret)
        return Catalog.afisare_lista()

    def __str__(self):
        return f'{self.nume}, {self.pret} lei, {self.gramaj} g'


class Tort(Catalog):
    def __init__(self, pret, gramaj):

        Catalog.__init__(self, "tort", pret, gramaj)
        self.etajat = False
        self.glazura = "ciocolata"

    def set_etaje(self, valoare):
        if type(valoare) == bool:
            self.etajat = valoare
        else:
            print("Introduceti True sau False")
            return

    def set_glazura(self, glazura):
        if type(glazura) == str:
            self.glazura =glazura
        else:
            print("Introduceti un text")
            return

    def __str__(self):
        return_string = Catalog.__str__(self)
        if self.etajat:
            etaje = "cu"
        else:
            etaje = "fara"
        return_string += f', glazura de {self.glazura}, {etaje} etaje'
        return return_string


class Fursec(Catalog):
    def __init__(self, pret, gramaj):
        Catalog.__init__(self, "fursec", pret, gramaj)


test = Catalog("leo", "abs", 40)
t1 = Tort(150, 3000)
t2 = Tort(200, 3500)
t3 = Tort(100, 2000)
f1 = Fursec(20, 100)
f2 = Fursec(35, 250)
f3 = Fursec(15, 150)
print(Catalog.sortare_gramaj())
print(Catalog.sortare_pret())

t1.set_etaje(True)
t1.set_glazura("cacao")
print(t1.__dict__)
print(t1)

t2.set_etaje(True)
t2.set_etaje(False)
t2.set_glazura("caramel")
print(t2)

print(Catalog.afisare_lista())




