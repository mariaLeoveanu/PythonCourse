from constants import months_digits, months_alpha, months_digits_short, counties_dictionary


# -------------- CHECK INPUT FUNCTIONS -----------

def check_gender(input_gender):
    genders = ("m", "f")
    if input_gender in genders:
        return True
    else:
        print("Invalid gender")
        return False


def check_year(input_year):
    if not input_year.isdigit():
        print("Invalid year of birth!")
        return False
    elif int(input_year) < 1800 or int(input_year) > 2099:
        print("Invalid year of birth!")
        return False
    else:
        return True


def check_month(input_month):
    if input_month not in months_digits and input_month not in months_alpha \
            and input_month not in months_digits_short:
        print("Invalid month of birth")
        return False
    else:
        return True


def check_day(input_day, input_month):
    short_month = "02"
    thirty_day_months = ("04", "06", "09", "11")
    thirty_one_day_months = ("01", "03", "05", "07", "08", "10", "12")
    if not input_day.isdigit():
        print("Invalid day of birth!")
        return False
    elif int(input_day) < 0:
        print("Invalid day of birth!")
        return False
    elif input_month in short_month and int(input_day) > 29:
        print("Invalid day of birth!")
        return False
    elif input_month in thirty_day_months and int(input_day) > 30:
        print("Invalid day of birth!")
        return False
    elif input_month in thirty_one_day_months and int(input_day) > 31:
        print("Invalid day of birth!")
        return False
    else:
        return True


def check_county(input_county):
    if input_county not in counties_dictionary.keys():
        print("Invalid county")
        return False
    else:
        return True


def check_cnp(input_cnp):
    if not input_cnp.isdigit() or len(input_cnp) != 13:
        print("CNP must be 13 characters and contain only numbers!")
        return False
    elif input_cnp[9:12:] == "000":
        print("CNP does not have a correct random number!")
        return False
    else:
        return True


def find_cnp_gender(input_gender, input_year, input_foreign, input_residence):
    input_year = int(input_year)
    if input_foreign == "y":
        if input_residence == "y":
            return "9"
        elif input_gender == "m":
            return "7"
        else:
            return "8"
    if 1900 <= input_year <= 1999:
        if input_gender == "m":
            return "1"
        else:
            return "2"
    elif 1800 <= input_year <= 1899:
        if input_gender == "m":
            return "3"
        else:
            return "4"
    elif 2000 <= input_year <= 2099:
        if input_gender == "m":
            return "5"
        else:
            return "6"


def check_cnp_header(cnp_hdr, actual_cnp):
    if cnp_hdr != actual_cnp[:9:]:
        print("The information you provided does not match the CNP!")
        return False
    else:
        return True


def checksum_cnp(input_cnp):
    nmb = str(279146358279)
    input_cnp = str(input_cnp)
    result = 0
    for n in range(12):
        result += int(nmb[n]) * int(input_cnp[n])
    result = result % 11
    if result == 10:
        result = 1
    print(result)
    return str(result)