import requests
from bs4 import BeautifulSoup
import pandas as pd

# TODO: test demo code for bs4

request = requests.get('https://www.bnr.ro/Cursul-de-schimb--7372.aspx')
response = request.text
link = BeautifulSoup(response, 'html.parser')
title = link.find_all('div', attrs={'class': 'contentDiv'})
# <table>
#     <thead>
#         <tr>
#             <th></th>
#             <th></th>
#         </tr>
#     </thead>
#     <tbody>
#         <tr>
#             <td></td>
#             <td></td>
#         </tr>
#         <tr>
#             <td></td>
#             <td></td>
#         </tr>
#     </tbody>
# </table>

header = []
data_list = []
set_td = set()
header_html = ''
tbody_html = ''
td = ''
tr = ''
table = ''
thead = ''

for i in title:
    for tr_index in i.find_all('table'):
        for td_index in tr_index.find_all('tr'):
            list_td = list()
            td = ''

            for th_index in td_index.find_all('th'):
                header.append(th_index.get_text())
                header_html += f'<th>{th_index.get_text()}</th>'
            thead = f'<thead><tr>{header_html}</tr></thead>'
            for trd_index in td_index.find_all('td'):
                list_td.append(tr_index.get_text().lstrip(' '))
                td += f'<td>{trd_index.get_text().lstrip(" ")}</td>'
            tr += f'<tr>{td}</tr>'
            data_list.append(tuple(list_td))

# html
table = f'<table>{thead}<tbody>{tr}</tbody></table>'
file = open('fileGoogle.html', 'w')
file.writelines(table)
file.close()

# excel
print(data_list)
df = pd.DataFrame(data_list, columns=header)
df.to_excel('Curs_BNR.xls', sheet_name='BNR', header=header, index=0)
"""
from selenium import webdriver
import pandas as pd
import matplotlib.pyplot as plt

browser = webdriver.Chrome('C:/webdrivers/chromedriver.exe')
browser.get('https://www.bnr.ro/files/xml/nbrfxrates2019.htm')
table = browser.find_element_by_xpath('//*[@id="Data_table"]')

# salvare in fisier
file = open('curs_valutar_bnr.txt', 'w+')
file.writelines(table.text)
file.close()

table = table.text
lista = table.split('\n')

header_len = browser.find_element_by_xpath('//*[@id="Data_table"]/table/thead/tr')
header = header_len.text.split('\n')
dictionar = {i: [] for i in header}
for j in range(0, len(header)):
    for i in range(len(header) + int(j), len(lista), len(header)):
        if '-' in lista[i]:
            dictionar[header[int(j)]].append(lista[i])
        else:
            dictionar[header[int(j)]].append(float(lista[i]))

df = pd.DataFrame(dictionar)
# import data to excel
df.to_excel("BNR_ALL_VALUES.xls")
browser.close()


a = header[3:9]
c = []
for i in range(3, 9):
    c.append(dictionar[header[int(i)]][int(i)])
d = sum(c)
e = []
for item in c:
    e.append(round(item/d*100))

colors = ['r', 'y', 'g', 'b', 'g', 'y']
plt.pie(e, labels=a, colors=colors, startangle=90, shadow=True, explode=(0.1, 0.1, 0.1, 0.1, 0.1, 0.2), radius=1.2, autopct='%1.1f%%')
plt.legend()
plt.show()"""



