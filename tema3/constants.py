
# --------------- CONSTANTS -----------------

months_digits = ("01",)
months_digits_short = ("1",)
months_alpha = ("january", "february", "march", "april", "may", "june", "july",
                "august", "september", "october", "november", "december")

for x in range(2, 10):
    months_digits = months_digits + ("0" + str(x),)
    months_digits_short = months_digits_short + (str(x),)
for x in range(10, 13):
    months_digits = months_digits + (str(x),)
    months_digits_short = months_digits_short + (str(x),)

counties_dictionary = {
    "alba": "01", "arad": "02", "arges": "03", "bacau": "04", "bihor": "05",
    "bistrita nasaud": "06", "botosani": "07", "brasov": "08", "braila": "09",
    "buzau": "10", "caras severin": "11", "cluj": "12", "constanta": "13",
    "covasna": "14", "dambovita": "15", "dolj": "16", "galati": "17",
    "gorj": "18", "harghita": "19", "hunedoara": "20", "ialomita": "21",
    "iasi": "22", "ilfov": "23", "maramures": "24", "mehedinti": "25",
    "mures": "26", "neamt": "27", "olt": "28", "prahova": "29", "satu mare": "30",
    "salaj": "31", "sibiu": "32", "suceava": "33", "teleorman": "34", "timis": "35",
    "tulcea": "36", "vaslui": "37", "valcea": "38", "vrancea": "39", "bucuresti": "40",
    "bucuresti, sector 1": "41", "bucuresti, sector 2": "42", "bucuresti, sector 3": "43",
    "bucuresti, sectorul 4:": "44", "bucuresti, sectorul 6": "46", "calarasi": "51",
    "giurgiu": "52"
}
