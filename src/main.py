from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#string de busca teste: BRAIN OR NEURO AND SOFTWARE DEVELOPMENT OR SOFTWARE ENGINEER

#Reference Variables 
CONST_ENTER_SEARCH_STRING = "Informe a string de busca:\n"
ACM_SEARCH_TERM_INPUT_COUNT = 0
ACM_ADD_SEARCH_TERM_BUTTON_COUNT = 1

#Receiveing search string from user
search_string = input(CONST_ENTER_SEARCH_STRING)
search_string_disjunctions = search_string.split(" AND ")
print(search_string_disjunctions)

#Initializing webdriver on Chrome Browser and accessing ACM Digital Library Advanced Search
acm_browser_webdriver = webdriver.Chrome()
acm_browser_webdriver.get("https://dl.acm.org/search/advanced")
element = WebDriverWait(acm_browser_webdriver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="pb-page-content"]/div/div/div[2]/a'))
)
acm_browser_webdriver.find_element(By.XPATH, '//*[@id="pb-page-content"]/div/div/div[2]/a').click()

#For each disjunction on the search string:
#Prepare the field camp that will receive the Keys
#Split the disjunction to get single terms
#Pass each term as a key to webdriver
for disjunction in search_string_disjunctions:
    #Increment to a new search term field 
    ACM_SEARCH_TERM_INPUT_COUNT += 1
    ACM_ADD_SEARCH_TERM_BUTTON_COUNT += 1

    #preparing web driver
    element = WebDriverWait(acm_browser_webdriver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="searchArea{}"]'.format(ACM_SEARCH_TERM_INPUT_COUNT)))
    )
    acm_browser_webdriver.find_element(by="xpath", value='//*[@id="searchArea{}"]'.format(ACM_SEARCH_TERM_INPUT_COUNT)).click()
    acm_browser_webdriver.find_element(by="xpath", value='//*[@id="searchArea{}"]/option[6]'.format(ACM_SEARCH_TERM_INPUT_COUNT)).click()
    acm_browser_webdriver.find_element(by="xpath", value='//*[@id="text{}"]'.format(ACM_SEARCH_TERM_INPUT_COUNT)).clear()

    print(disjunction)
    #spliting the disjunctions
    string_terms = disjunction.split(" OR ")

    #passing each term as a key
    terms_amount = len(string_terms)
    for i in range(terms_amount):
        acm_browser_webdriver.find_element(by="xpath", value='//*[@id="text{}"]'.format(ACM_SEARCH_TERM_INPUT_COUNT)).send_keys('"{}"'.format(string_terms[i]))
        if (i + 1 < terms_amount): acm_browser_webdriver.find_element(by="xpath", value='//*[@id="text{}"]'.format(ACM_SEARCH_TERM_INPUT_COUNT)).send_keys(' OR ')

    acm_browser_webdriver.find_element(by="xpath", value='//*[@id="frmSearch"]/div[2]/div/div[{}]/a[1]'.format(ACM_ADD_SEARCH_TERM_BUTTON_COUNT)).click()

#Click the search button:
acm_browser_webdriver.find_element(by="xpath", value='//*[@id="frmSearch"]/div[5]/div/div[2]/button').click()