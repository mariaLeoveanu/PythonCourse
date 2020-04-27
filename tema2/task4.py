number = int(input("Introduceti un numar: "))
if number > 0:
    if number < 10:
        print("Numarul este mai mic decat 10")
    else:
        print("Numarul este mai mare ca 10.")
elif number == 0:
    print("Numarul este 0.")
else:
    output = "Numarul este negativ. Modulul sau este {0}.".format(number * -1)
    print(output)
