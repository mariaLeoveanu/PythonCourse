cuvant = 'abcde'
print(cuvant[0])
print(cuvant[6])  # eroare
print(cuvant[6:])  # slicing-ul previne aparitia unei erori
print(cuvant[-1])  # proceseaza caracterul de la sfarsit la inceput
# -2 va afisa 'd', indexarea de la final incepe de la -1, nu de la 0

# modificarea unui caracter din string
print(cuvant.replace('d', 'f'))  # se afiseaa modificat
print(cuvant)  # cuvantul e la fel

cuvant = cuvant.replace('d', 'f')  # cuvantul primeste o noua valoare

# cautarea unui caracter intr-un sir de caractere
if 'b' in cuvant:
    print("Am gasit caracterul b")
cuvant.find('b')  # returneaza indexul la care se gaseste caracterul, -1 daca nu exista

# split
print(cuvant.split('c'))  # returneaza ce e inainte de c si ce e dupa c ca o lista
print("".join(cuvant.split('c')))  # reuneste elementele rezultate

# tupluri

tupl = (1, )
print(type(tupl))  # returneaza int daca tupl = (1), <tuple> daca tupl = (1, )

tupl = tupl + (2, 3, 4)
print(tupl)  # concatenare de tupluri

# accesarea unui index dintr-un tuplu
print(tupl[2])

# modificarea unei valori dintr-un tuplu !! nu se poate
# un tuplu = immutable




