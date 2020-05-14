from selenium import webdriver


def send_text_to_input(name_input, text):
    # gaseste field-ul din pagina dupa nume
    field = driver.find_element_by_name(name_input)
    field.send_keys(text)


# ca parametru punem calea locala pt driver
driver = webdriver.Chrome('C:/webdrivers/chromedriver.exe')
driver.maximize_window()
driver.get("https://www.cel.ro/index.php?main_page=login")

send_text_to_input("firstname", "Test")
send_text_to_input("lastname", "Test")
send_text_to_input("email_address", "maria.leoveanu@yahoo.com")
send_text_to_input("telephone", "1234567")
send_text_to_input("street_address", "Strada 1")
send_text_to_input("entry_suburb", "Bucuresti")
send_text_to_input("city", "Bucuresti")

# prentru bifarea termenilor si conditiilor
# cautam id-ul butonului

get_button = driver.find_element_by_name("termeni")
get_button.click()
# in pagina web pentru buton exista valorile on/off
# pentru a bifa, setam starea butonului pe on


# apeland .submit() pe oricare dintre elemente trimitem formularul
