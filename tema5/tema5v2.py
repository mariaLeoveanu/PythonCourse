from selenium import webdriver
import pandas as pd
import matplotlib.pyplot as plt

table_content = {i: [] for i in range(1, 43)}
browser = webdriver.Chrome('C:/webdrivers/chromedriver.exe')
table_columns = ['Judet']
for date in range(3, 25):
    browser.get('https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-' + str(date) + '-aprilie-2020-ora-13-00/')
    table = browser.find_element_by_tag_name('table').find_elements_by_tag_name('tbody')
    columns = table[0].find_elements_by_tag_name('strong')
    if len(columns) != 0:
        table_columns.append(f'{date} aprilie 2020')
        rows = table[0].find_elements_by_tag_name('tr')
        for row in rows[1:len(rows) - 1]:
            cells = row.find_elements_by_tag_name('td')
            id_county = int(cells[0].text.rstrip('.'))
            county = cells[1].text
            cases = int(cells[2].text.replace('.', ''))
            if id_county <= 42:
                if county not in table_content[id_county]:
                    table_content[id_county].append(county)
                table_content[id_county].append(cases)


print(table_content)
all_rows = []
for j in range(1, 43):
    all_rows.append(list(table_content[j]))
df = pd.DataFrame(all_rows)
df.to_excel('TABEL_COMPLET.xls', header=table_columns)
browser.close()

tr_header = ''
for col in table_columns:
    tr_header += f'<th>{col}</th>'
tr_body = ''
for row in table_content:
    row_html = ''
    for cell in table_content[row]:
        row_html += f'<td>{cell}</td>'
    tr_body += f'<tr>{row_html}</tr>'

html_table = f'<meta http-equiv="Content-Type" content="text/html; charset=UTF-8"><table>{tr_header}<tbody>{tr_body}</tbody></table>'
file = open('final_table.html', 'w', encoding='utf-8')
file.writelines(html_table)
file.close()

