name = input("Nume: ")
inputString = input("Text: ")
if inputString.isdigit():
    print("Sirul de numere a fost gasit de" + name)
elif inputString.isalpha():
    print("Sirul de caractere a fost gasit de " + name)
else:
    print("Sirul mixt a fost gasit de " + name)