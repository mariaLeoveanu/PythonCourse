import datetime


def message():
    print("Enter value")


# apelarea functiei
# message()


def hello(param_name='Leo'):
    print("hello", param_name)


# = 'Leo' = valoare default =>
# se poate apela hello()
# name = input("Enter name: ")
# hello(name)

# se suprascrie variabila message
# message() nu mai functioneaza
message = 1


def print_nmb(what='phone', nmb='2'):
    # exemplu documentare functii
    """
    :param what:
    :param nmb:
    :return:
    """
    print("enter", what, "number", nmb)


# print_nmb("ABC", '5')
# parametri se pot trimite in alta ordine cu aceasta notatie
# print_nmb(nmb='4', what='number')


def sum_of_numbers(a, b, c):
    print(f'{a} + {b} + {c} = ', a+b+c)


# sum_of_numbers(1, 2, 3)
# parametrii se atribuie in ordine in cazul in care nu au toti notatia param=
# sum_of_numbers(3, a=1, b=2)

# sum_of_numbers(2, c=2, b=5) functioneaza deoarece a e pe prima pozitie si valoarea se atribuie corect


def lma(wishes=True):
    print('3')
    print('2')
    print('1')
    if not wishes:
        return
    print("lma")


# print(lma(False))  # afiseaza none: o functie care nu returneaza int/etc returneaza by default None


def name():
    return 123


a = name
# print(a)  # afiseaza valoarea 123 returnata de functia name()


def sum_of_list(lst):
    sum = 0
    for elem in lst:
        sum += elem
    return sum


# daca indentam return sum => se afiseaza 1 si se iese din functie
# a = sum_of_list([1, 2, 3])  # returneaza 12 si apoi se iese


def litere(litera:str) -> bool:
    if isinstance(litera, str):
        return True
    else:
        return '23'

# !! linia din semnatura functiei reprezinta o recomandare pt tipurile de date primite/returnate
# !! functia functioneaza ok si cum e scris mai sus, dar nu e un comportament recomandat


def validare_nr_zile(zi, luna, an) -> bool:
    try:
        a = datetime.datetime.strptime(f'{zi}.{luna}.{an}', '%d.%m.%Y')
    except Exception as e:
        return False
    else:
        pass
    finally:
        print("Data este ", zi, luna, an)


# except: mod de gestionare al unui caz de eroare
# finally se executa indif daca apar exceptii sau nu
# else: se executa daca nu apar exceptii
# a = validare_nr_zile(23, 7, 2000)
# print(a)


def is_prime(number:int) -> bool:
    i = 3
    if number < 2:
        return False
    elif number == 2:
        return True
    else:
        i = 2
        while i * i <= number:
            if number % i == 0:
                return False
            i += 1
        return True


# print(is_prime(4))
# print(is_prime(3))
# print(is_prime(11))


def scopes():
    # global var
    var = 2
    # !! global -> var face referire la variabila var globala
    print('Var este:', var)


# var = 1
# scopes()
# print(var)




