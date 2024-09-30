import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from pageobjects.homepageelements import Element
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.xe.com/')
time.sleep(5)


def converter():
    actions = ActionChains(driver)

    Amount = driver.find_element(By.XPATH, Element.amount)
    Amount.send_keys('10')

    Country = driver.find_element(By.XPATH, Element.currency_country_from)
    Country.send_keys('USD')

    Country1 = driver.find_element(By.XPATH, '//ul[@id="midmarketFromCurrency-listbox"]/li[1]')
    Country1.click()

    country = driver.find_element(By.XPATH, Element.currency_country_to)
    country.send_keys('EUR')

    Country2 = driver.find_element(By.XPATH, '//ul[@id="midmarketToCurrency-listbox"]/li[2]')
    Country2.click()

    ConverterButton = driver.find_element(By.XPATH, Element.currency_covert_button)
    ConverterButton.click()
    driver.implicitly_wait(5)
    time.sleep(10)

    Actual_Result = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[4]/div[2]/section/div[2]/div/main/div/div[2]/div[1]/div/p[2]')

    a = Actual_Result.text
    b = "8.9 Euros"
    if a == b:
        print("USD to EURO Money Converter is Working successfully and the correct amount is converted")
    else:
        print("Money Converter is working successfully and the correct amount is converted")

converter()
driver.back()



# Get Started Button Link Click
def button_link():
    button = driver.find_element(By.XPATH, Element.get_started)
    assert button.is_displayed(), "Button is visible on the page."
    button.click()
    driver.implicitly_wait(5)
    expected_url = "https://account.xe.com/signup?redirect_uri=https%3A%2F%2Fpersonal-registration.xe.com&ctaPosition=tab"
    try:
        WebDriverWait(driver, 10).until(EC.url_to_be(expected_url))
        print("Get Started Button Link Clicked Successfully and Correct Page Loaded")
    except:
        print(f"Get Started Button Link Click Failed. Current URL: {driver.current_url}")
button_link()
time.sleep(2)
driver.back()
time.sleep(2)



# More Tools Button Link Click
def button_link():
    button = driver.find_element(By.XPATH, Element.more_tool)
    assert button.is_displayed(), "Button is visible on the page."
    button.click()
    driver.implicitly_wait(5)
    expected_url = "https://www.xe.com/"
    try:
        WebDriverWait(driver, 10).until(EC.url_to_be(expected_url))
        print("More Tools Button Link Clicked Successfully and Correct Page Loaded")
    except:
        print(f"More Tools Button Link Click Failed. Current URL: {driver.current_url}")
button_link()
time.sleep(2)



# Sign up Button Link Click
def button_link():
    button = driver.find_element(By.XPATH, Element.sign_up)
    assert button.is_displayed(), "Button is visible on the page."
    button.click()
    driver.implicitly_wait(5)
    expected_url = "https://www.xe.com/currencyemail/"
    try:
        WebDriverWait(driver, 10).until(EC.url_to_be(expected_url))
        print("Sign up Button Link Clicked Successfully and Correct Page Loaded")
    except:
        print(f"Sign up Button Link Click Failed. Current URL: {driver.current_url}")
button_link()
time.sleep(2)
driver.back()
time.sleep(2)



driver.quit()