number = input("Introduceti un numar: ")
if not number.isdigit():
    print("Nu ati introdus un numar.")
else:
    number = int(number)
    if number % 2 == 0:
        print("Numarul este par.")
    else:
        print("Numarul este impar.")
