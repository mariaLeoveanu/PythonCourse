# === SIRURI DE CARACTERE ===

# escape charcters: \ inainte de caracter
# pt tab \t, pt spatiu nou \n sau ghilimele triple

print("Primul meu string\"lalal\"")

# * n afiseaza de n ori stringul
# ordinea matematica

print(2 + 2 * 2 - 2 / 1)

# ridicare la putere -> **

# === VARIABILE ===
a = "String"
a += 'String1'
print(a)
print(type(a))

# concatenare cu format

a = "string1"
b = "string1"
c = "al treilea"
c = "{1} {0} {1} {2}".format(a, b, c)
print("Concatenare cu format: " + c)

# 1 si 0 din acolade reprezinta ordindea in care se afiseaza

# concatenare cu fstring

c = f"{a} {b}"
print("Concatenare cu fstring " + c)

# === TIPURI DE DATE ===

a = 1
b = 2
c = a + b
print(c)
# rezultatul e int, daca punem nr intre ghilimele => string
# !! diferit f de JAVA, nu se poate concatena un nr cu un string

a = input("Nume si prenume: ")
print(a)

num1 = int(input("Primul numar: "))
num2 = int(input("Al doilea numar: "))
sum12 = num1 + num2
print(sum12)

# a e de tip string => trb facuta parsarea inainte (ex pt inturi)

# === INTSTRUCTIUNI ===

# === IF ===

# if cond1 : ex1
# elif cond2 : ex2
# else ex3

a = 2
b = 2
print("Adresa a: " + hex((id(a))))
print("Adresa b: " + hex((id(b))))
# aici adresele sunt la fel

b += 1
# adresele sunt diferite pt a si b dupa ce b se modifica

if a:
    print("a este adv")

# a = None inseamna ca a nu are nicio valoare

a = 2
b = 3

if a is b:
    print("a e egal cu b")
elif a > b:
    print("a e mai mare")
else:
    print("a e mai mic")

# === WHILE ===

# while cond:
# cmd1
# ...
# cmdn

x = 5
while x > 1:
    print("x = ", x)
    # x -= 1
    break  # break la fel ca in Java

a = 2
b = 2 if a == 2 else 3  # atribuire conditionata

while True:
    print("Apasati 1 pentru a face conversie")
    print("Apasati 2 pentru a iesi din bucla")
    ok = input()
    if ok.isdigit() and int(ok) == 1:
        euro = input("Suma euro: ")
        if euro.isdigit():
            print("Valoare conversie: ", int(euro) * 4.87, "RON")
        elif len(euro.split('.')) == 2 and euro.split('.')[0].isdigit() and euro.split('.')[1].isdigit():
            print("Valoare conversie: ", float(euro) * 4.87, "RON")
        else:
            print("Introduceti un numar")
    else:
        break

string = "abecedar"

print(string[-1])
print(string[::2])  # afiseaza literele din 2 in 2
print(string[2::])  # afiseaza de la litera de index 2 toate literele

# === FOR ===

for poz, char in enumerate(string):
    print(poz, char)
# afiseaza pozitie + caracter din stringul string

for x in range(6):
    print(x)  # de la 0 la 5
for x in range(-1, 6, 2):
    print(x)  # de la -1 la 5 cu pasul 2

lista = [x for x in range(10)]  # lista cu elem de la 0 la 9