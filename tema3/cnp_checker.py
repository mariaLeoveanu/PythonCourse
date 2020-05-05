from check_functions import check_gender, check_year, check_month, check_day, \
    check_county, check_cnp, find_cnp_gender, \
    check_cnp_header, checksum_cnp
from constants import months_digits, months_alpha, months_digits_short, counties_dictionary

# --------- MAIN CODE ------------
while True:
    gender = input("Gender: ")
    gender = gender.lower()
    if check_gender(gender):
        break

while True:
    birth_year = input("Year of birth: ")
    if check_year(birth_year):
        break

while True:
    birth_month = input("Month of birth: ")
    birth_month = birth_month.lower()
    if check_month(birth_month):
        break

# convert month from whatever input to the one which will be added in CNP
if birth_month in months_alpha:
    birth_month = months_digits[months_alpha.index(birth_month)]
elif birth_month in months_digits_short:
    birth_month = months_digits[months_digits_short.index(birth_month)]

while True:
    birth_day = input("Day of birth: ")
    if check_day(birth_day, birth_month):
        break

# format days 1->9
if len(birth_day) == 1:
    birth_day = "0" + birth_day

while True:
    birth_county = input("County: ")
    birth_county = birth_county.lower()
    if birth_county == "bucuresti":
        while True:
            sct = input("Sector: ")
            if sct.isdigit() and 1 <= int(sct) <= 6:
                break
            else:
                print("Please enter a valid sector: 1-6")
        # create key value for county dictionary
        birth_county += ", sector " + sct
    if check_county(birth_county):
        break

while True:
    cnp = input("CNP: ")
    if check_cnp(cnp):
        break

# additional information for foreign citizens
while True:
    foreign = input("Are you of a foreign nationality? (not Romanian) Y/N: ")
    foreign = foreign.lower()
    if foreign == "y" or foreign == "n":
        break
    else:
        print("Please enter a valid input: Y/N: ")

while True:
    residence = input("Do you live in Romania? Y/N: ")
    residence = residence.lower()
    if residence == "y" or residence == "n":
        break
    else:
        print("Please enter a valid input: Y/N")

# create the header with given information and check if it coincides with given CNP
cnp_header = find_cnp_gender(gender, birth_year, foreign, residence)
cnp_header += birth_year[2:]
cnp_header += birth_month
cnp_header += birth_day
cnp_header += str(counties_dictionary.get(birth_county))

if check_cnp(cnp) and check_cnp_header(cnp_header, cnp) and checksum_cnp(cnp) == cnp[12]:
    print("The CNP you provided is valid!")
else:
    print("The CNP you provided is not correct")
