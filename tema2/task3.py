an = input("Introduceti un an: ")
if not an.isdigit():
    print("Nu ati introdus un numar")
else:
    if an % 4 == 0:
        print("Anul este bisect.")
    else:
        print("Anul nu este bisect.")
