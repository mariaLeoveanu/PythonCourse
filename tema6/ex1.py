class Catalog:
    def __init__(self, nume, prenume):
        if type(nume) == str and type(prenume) == str:
            self.catalog = {}
            self.absente = 0
            self.nume = nume
            self.prenume = prenume
        else:
            print("Introduceti valori text pentru nume si prenume")
            return

    def __str__(self):
        return f'Absente {self.nume} {self.prenume}: {self.absente}'

    def adaugare_absenta(self, number=1):
        if type(number) == int:
            self.absente += number
        else:
            print("Intoduceti un numar")
            return

    def motivare_absente(self, number=1):
        if type(number) == int:
            self.absente = max(self.absente - number, 0)
        else:
            print("Introduceti un numar")


class Materii(Catalog):
    def adaugare_materie(self, materie, note):
        self.catalog[materie] = note

    def afisare_materii(self):
        return_string = ''
        for materie in self.catalog:
            return_string += materie + " "
        return return_string

    def afisare_medii(self):
        return_str = ''
        for materie in self.catalog:
            medie = 0
            length = 0
            for nota in self.catalog[materie]:
                if type(nota) == int:
                    medie += nota
                    length += 1
            medie = medie / length
            return_str += f'{materie}: {medie}\n'
        return return_str


student1 = Materii("Ion", "Roata")
student1.adaugare_absenta()
student1.adaugare_absenta(3)
student1.motivare_absente(2)
student2 = Materii("George", "Cerc")
student2.adaugare_absenta(4)
student2.motivare_absente(2)
print(student1)
print(student2)


student1.adaugare_materie("Python", [6, 10, 8, (2, 3)])
student2.adaugare_materie("Python", [5, 7, 4, True])
student1.adaugare_materie("Romana", [9, 9, 10])
student2.adaugare_materie("Matematica", [10, 9, 8, "text0"])

print(student1.afisare_medii())
print(student1.afisare_materii())

print(student2.afisare_medii())
print(student2.afisare_materii())















