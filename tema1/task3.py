an = input("Introduceti un an: ")
if not an.isdigit():
    print("Nu ati introdus un numar")
else:
    an = int(an)
    if an % 4 == 0:
        print("Anul este bisect.")
    else:
        print("Anul nu este bisect.")
