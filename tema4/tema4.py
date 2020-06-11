import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt

writer = pd.ExcelWriter("PrimulTabel.xls")
counties = {i: [] for i in range(1, 44)}
non_empty_dates = []
counties_list = ["Placeholder"]

for i in range(3, 25):

    request = requests.get('https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-' + str(i) + '-aprilie-2020-ora-13-00/').text
    soup = BeautifulSoup(request, 'lxml')
    table = soup.table

    column_names = table.tbody.tr.find_all('td')
    column_text = []

    # extract the text from each <strong> tag
    for name in column_names:
        try:
            column_text.append(name.strong.text)
            table_content = []
        except AttributeError:
            pass

    if len(column_text) > 0:

        non_empty_dates.append(i)

        # get all counties
        # from 1 to skip the name of the rows
        # skip the total row
        for entry in table.find_all("tr")[1:len(table.find_all('tr')) - 1:]:
            line_text = list()

            # update content for each table
            line_text.append(str(i) + " aprilie 2020")
            line_text.append(int(entry.find_all('td')[2].text.replace(".", '')))
            table_content.append(tuple(line_text))

            current_county = entry.find_all('td')[1].text
            if current_county not in counties_list:
                counties_list.append(current_county)

            # store in the dictionary for each county the nmb. of cases
            counties[int(entry.find('td').text.rstrip('.'))].append(tuple(line_text))

start = 1
county_id = {}
# for all counties
for i in range(1, 44):

    county_id[list(counties_list)[start]] = start
    # replace one name of column
    column_text[1] = "Date"

    df = pd.DataFrame(counties[start], columns=column_text[1::])
    df.to_excel(writer, sheet_name=list(counties_list)[start], header=column_text[1::], index=0)
    start += 1

writer.save()
writer.close()

request_html = input("Introduceti numele unui judet:")
if request_html not in county_id:
    print("Nu a fost gasit judetul ", request_html)
else:

    html_header = ''
    thead = ''
    tr = ''
    html_body = ''

    for column in column_text[1::]:
        html_header += f'<th>{column}</th>'

    thead = f'<thead><tr>{html_header}</tr></thead>'
    for row in counties[county_id[request_html]]:
        td = ''
        for cell in row:
            td += f'<td>{cell}</td>'
        tr += f'<tr>{td}</tr>'

    html_body = f'<tbody>{tr}</tbody>'

    html = f'<table>{thead}{html_body}</table>'
    file = open(request_html + ".html", 'w')
    file.writelines(html)
    file.close()

request_graph = input("Intoduceti un judet:")
if request_graph not in county_id:
    print("Nu a fost gasit judetul ", request_html)
else:
    all_numbers = []
    for num in counties[county_id[request_html]]:
        all_numbers.append(num[1])
    plt.plot(non_empty_dates, all_numbers)
    plt.xticks(non_empty_dates)
    plt.xlabel(f'Evolutia cazurilor in {request_graph} in intervalul 3-24 aprilie')
    plt.show()


