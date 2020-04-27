command1 = "Afisare lista de cumparaturi"
command2 = "Adaugare element"
command3 = "Stergere element"
command4 = "Stergere lista de cumparaturi"
command5 = "Cautare in lista de cumparaturi"
instructions = "1 - {0}\n2 - {1}\n3 - {2}\n4 - {3}\n5 - {4}".format(command1, command2, command3, command4, command5)
print(instructions)
while 1:
    number = int(input("Introduceti o comanda: "))
    if number == 1:
        print(command1)
    elif number == 2:
        print(command2)
    elif number == 3:
        print(command3)
    elif number == 4:
        print(command4)
    elif number == 5:
        print(command5)
    else:
        print("Alegerea nu exista. Reincercati!")