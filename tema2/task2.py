number = input("Introduceti un numar: ")
if not number.isalpha():
    print("Nu ati introdus un numar.")
else:
    if number % 2 == 0:
        print("Numarul este par.")
    else:
        print("Numarul este impar.")
