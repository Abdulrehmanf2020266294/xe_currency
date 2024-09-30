import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from pageobjects.homepageelements import Element
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.get("https://www.xe.com/")
driver.maximize_window()
time.sleep(4)



# USA-US Dollar Link Click in Footer
def footer_link():
    button = driver.find_element(By.XPATH, Element.usa_footer)
    assert button.is_displayed(), "Button is visible on the page."
    time.sleep(2)
    button.click()
    driver.implicitly_wait(5)
    expected_url = "https://www.xe.com/currency/usd-us-dollar/"
    try:
        WebDriverWait(driver, 10).until(EC.url_to_be(expected_url))
        print("USA-US Dollar Link Clicked Successfully and Correct Page Loaded")
    except:
        print(f"USA-US Dollar Link Click Failed. Current URL: {driver.current_url}")
footer_link()
time.sleep(2)
driver.back()
time.sleep(2)



# EUR - Euro Link Click in Footer
def footer_link():
    button = driver.find_element(By.XPATH, Element.euro_footer)
    assert button.is_displayed(), "Button is visible on the page."
    button.click()
    driver.implicitly_wait(5)
    expected_url = "https://www.xe.com/currency/eur-euro/"
    try:
        WebDriverWait(driver, 10).until(EC.url_to_be(expected_url))
        print("EUR - Euro Link Clicked Successfully and Correct Page Loaded")
    except:
        print(f"EUR - Euro Link Click Failed. Current URL: {driver.current_url}")
footer_link()
time.sleep(2)
driver.back()
time.sleep(2)


# GBP - British Pound Link Click in Footer
def footer_link():
    button = driver.find_element(By.XPATH, Element.gbp_footer)
    assert button.is_displayed(), "Button is visible on the page."
    button.click()
    driver.implicitly_wait(5)
    expected_url = "https://www.xe.com/currency/gbp-british-pound/"
    try:
        WebDriverWait(driver, 10).until(EC.url_to_be(expected_url))
        print("GBP - British Pound Link Clicked Successfully and Correct Page Loaded")
    except:
        print(f"GBP - British Pound Link Click Failed. Current URL: {driver.current_url}")
footer_link()
time.sleep(2)
driver.back()
time.sleep(2)



# CAD - Canadian Dollar Link Click in Footer
def footer_link():
    button = driver.find_element(By.XPATH, Element.cad_footer)
    assert button.is_displayed(), "Button is visible on the page."
    button.click()
    driver.implicitly_wait(5)
    expected_url = "https://www.xe.com/currency/cad-canadian-dollar/"
    try:
        WebDriverWait(driver, 10).until(EC.url_to_be(expected_url))
        print("CAD - Canadian Dollar Link Clicked Successfully and Correct Page Loaded")
    except:
        print(f"CAD - Canadian Dollar Link Click Failed. Current URL: {driver.current_url}")
footer_link()
time.sleep(2)
driver.back()
time.sleep(2)



# AUD - Australian Dollar Link Click in Footer
def footer_link():
    button = driver.find_element(By.XPATH, Element.aud_footer)
    assert button.is_displayed(), "Button is visible on the page."
    time.sleep(2)
    button.click()
    driver.implicitly_wait(5)
    expected_url = "https://www.xe.com/currency/aud-australian-dollar/"
    try:
        WebDriverWait(driver, 10).until(EC.url_to_be(expected_url))
        print("AUD - Australian Dollar Link Clicked Successfully and Correct Page Loaded")
    except:
        print(f"AUD - Australian Dollar Link Click Failed. Current URL: {driver.current_url}")
footer_link()
time.sleep(2)
driver.back()
time.sleep(2)



# JPY - Japanese Yen Link Click in Footer
def footer_link():
    button = driver.find_element(By.XPATH, Element.jpy_footer)
    assert button.is_displayed(), "Button is visible on the page."
    time.sleep(2)
    button.click()
    driver.implicitly_wait(5)
    expected_url = "https://www.xe.com/currency/jpy-japanese-yen/"
    try:
        WebDriverWait(driver, 10).until(EC.url_to_be(expected_url))
        print("JPY - Japanese Yen Link Clicked Successfully and Correct Page Loaded")
    except:
        print(f"JPY - Japanese Yen Link Click Failed. Current URL: {driver.current_url}")
footer_link()
time.sleep(2)
driver.back()
time.sleep(2)



# INR - Indian Rupee Link Click in Footer
def footer_link():
    button = driver.find_element(By.XPATH, Element.inr_footer)
    assert button.is_displayed(), "Button is visible on the page."
    time.sleep(2)
    button.click()
    driver.implicitly_wait(5)
    expected_url = "https://www.xe.com/currency/inr-indian-rupee/"
    try:
        WebDriverWait(driver, 10).until(EC.url_to_be(expected_url))
        print("INR - Indian Rupee Link Clicked Successfully and Correct Page Loaded")
    except:
        print(f"INR - Indian Rupee Link Click Failed. Current URL: {driver.current_url}")
footer_link()
time.sleep(2)
driver.back()
time.sleep(2)




# NZD - New Zealand Dollar Link Click in Footer
def footer_link():
    button = driver.find_element(By.XPATH, Element.nzd_footer)
    assert button.is_displayed(), "Button is visible on the page."
    time.sleep(2)
    button.click()
    driver.implicitly_wait(5)
    expected_url = "https://www.xe.com/currency/nzd-new-zealand-dollar/"
    try:
        WebDriverWait(driver, 10).until(EC.url_to_be(expected_url))
        print("NZD - New Zealand Dollar Link Clicked Successfully and Correct Page Loaded")
    except:
        print(f"NZD - New Zealand Dollar Link Click Failed. Current URL: {driver.current_url}")
footer_link()
time.sleep(2)
driver.back()
time.sleep(2)



# CHF - Swiss Franc Link Click in Footer
def footer_link():
    button = driver.find_element(By.XPATH, Element.chf_footer)
    assert button.is_displayed(), "Button is visible on the page."
    time.sleep(2)
    button.click()
    driver.implicitly_wait(5)
    expected_url = "https://www.xe.com/currency/chf-swiss-franc/"
    try:
        WebDriverWait(driver, 10).until(EC.url_to_be(expected_url))
        print("CHF - Swiss Franc Link Clicked Successfully and Correct Page Loaded")
    except:
        print(f"CHF - Swiss Franc Link Click Failed. Current URL: {driver.current_url}")
footer_link()
time.sleep(2)
driver.back()
time.sleep(2)


# ZAR - South African Rand Link Click in Footer
def footer_link():
    button = driver.find_element(By.XPATH, Element.zar_footer)
    assert button.is_displayed(), "Button is visible on the page."
    time.sleep(2)
    button.click()
    driver.implicitly_wait(5)
    expected_url = "https://www.xe.com/currency/zar-south-african-rand/"
    try:
        WebDriverWait(driver, 10).until(EC.url_to_be(expected_url))
        print("ZAR - South African Rand Link Clicked Successfully and Correct Page Loaded")
    except:
        print(f"ZAR - South African Rand Link Click Failed. Current URL: {driver.current_url}")
footer_link()
time.sleep(2)
driver.back()
time.sleep(2)


# RUB - Russian Ruble Link Click in Footer
def footer_link():
    button = driver.find_element(By.XPATH, Element.rub_footer)
    assert button.is_displayed(), "Button is visible on the page."
    time.sleep(2)
    button.click()
    driver.implicitly_wait(5)
    expected_url = "https://www.xe.com/currency/rub-russian-ruble/"
    try:
        WebDriverWait(driver, 10).until(EC.url_to_be(expected_url))
        print("RUB - Russian Ruble Link Clicked Successfully and Correct Page Loaded")
    except:
        print(f"RUB - Russian Ruble Link Click Failed. Current URL: {driver.current_url}")
footer_link()
time.sleep(2)
driver.back()
time.sleep(2)



# BGN - Bulgarian Lev Link Click in Footer
def footer_link():
    button = driver.find_element(By.XPATH, Element.bgn_footer)
    assert button.is_displayed(), "Button is visible on the page."
    time.sleep(2)
    button.click()
    driver.implicitly_wait(5)
    expected_url = "https://www.xe.com/currency/bgn-bulgarian-lev/"
    try:
        WebDriverWait(driver, 10).until(EC.url_to_be(expected_url))
        print("BGN - Bulgarian Lev Link Clicked Successfully and Correct Page Loaded")
    except:
        print(f"BGN - Bulgarian Lev Link Click Failed. Current URL: {driver.current_url}")
footer_link()
time.sleep(2)
driver.back()
time.sleep(2)




# Send Money Online Link Click in Footer
def footer_link():
    button = driver.find_element(By.XPATH, Element.send_money_online_footer)
    assert button.is_displayed(), "Button is visible on the page."
    time.sleep(2)
    button.click()
    driver.implicitly_wait(5)
    expected_url = "https://www.xe.com/send-money/"
    try:
        WebDriverWait(driver, 10).until(EC.url_to_be(expected_url))
        print("Send Money Online Link Clicked Successfully and Correct Page Loaded")
    except:
        print(f"Send Money Online Link Click Failed. Current URL: {driver.current_url}")
footer_link()
time.sleep(2)
driver.back()
time.sleep(2)



# Send Money to India Link Click in Footer
def footer_link():
    button = driver.find_element(By.XPATH, Element.send_money_ind)
    assert button.is_displayed(), "Button is visible on the page."
    time.sleep(2)
    button.click()
    driver.implicitly_wait(5)
    expected_url = "https://www.xe.com/send-money/send-money-to-india/"
    try:
        WebDriverWait(driver, 10).until(EC.url_to_be(expected_url))
        print("Send Money to India Link Clicked Successfully and Correct Page Loaded")
    except:
        print(f"Send Money to India Link Click Failed. Current URL: {driver.current_url}")
footer_link()
time.sleep(2)
driver.back()
time.sleep(2)




# Send Money to Pakistan Link Click in Footer
def footer_link():
    button = driver.find_element(By.XPATH, Element.send_money_pak)
    assert button.is_displayed(), "Button is visible on the page."
    time.sleep(2)
    button.click()
    driver.implicitly_wait(5)
    expected_url = "https://www.xe.com/send-money/send-money-to-pakistan/"
    try:
        WebDriverWait(driver, 10).until(EC.url_to_be(expected_url))
        print("Send Money to Pakistan Link Clicked Successfully and Correct Page Loaded")
    except:
        print(f"Send Money to Pakistan Link Click Failed. Current URL: {driver.current_url}")
footer_link()
time.sleep(2)
driver.back()
time.sleep(2)


# Send Money to Mexico Link Click in Footer
def footer_link():
    button = driver.find_element(By.XPATH, Element.send_money_mexico)
    assert button.is_displayed(), "Button is visible on the page."
    time.sleep(2)
    button.click()
    driver.implicitly_wait(5)
    expected_url = "https://www.xe.com/send-money/send-money-to-mexico/"
    try:
        WebDriverWait(driver, 10).until(EC.url_to_be(expected_url))
        print("Send Money to Mexico Link Clicked Successfully and Correct Page Loaded")
    except:
        print(f"Send Money to Mexico Link Click Failed. Current URL: {driver.current_url}")
footer_link()
time.sleep(2)
driver.back()
time.sleep(2)



# Send Money to Japan Link Click in Footer
def footer_link():
    button = driver.find_element(By.XPATH, Element.send_money_japan)
    assert button.is_displayed(), "Button is visible on the page."
    time.sleep(2)
    button.click()
    driver.implicitly_wait(5)
    expected_url = "https://www.xe.com/send-money/send-money-to-japan/"
    try:
        WebDriverWait(driver, 10).until(EC.url_to_be(expected_url))
        print("Send Money to Japan Link Clicked Successfully and Correct Page Loaded")
    except:
        print(f"Send Money to Japan Link Click Failed. Current URL: {driver.current_url}")
footer_link()
time.sleep(2)
driver.back()
time.sleep(2)



# Send Money to the UK Link Click in Footer
def footer_link():
    button = driver.find_element(By.XPATH, Element.send_money_uk)
    assert button.is_displayed(), "Button is visible on the page."
    time.sleep(2)
    button.click()
    driver.implicitly_wait(5)
    expected_url = "https://www.xe.com/send-money/send-money-to-united-kingdom/"
    try:
        WebDriverWait(driver, 10).until(EC.url_to_be(expected_url))
        print("Send Money to the UK Link Clicked Successfully and Correct Page Loaded")
    except:
        print(f"Send Money to the UK Link Click Failed. Current URL: {driver.current_url}")
footer_link()
time.sleep(2)
driver.back()
time.sleep(2)



# Send Money to Canada Link Click in Footer
def footer_link():
    button = driver.find_element(By.XPATH, Element.send_money_canada)
    assert button.is_displayed(), "Button is visible on the page."
    time.sleep(2)
    button.click()
    driver.implicitly_wait(5)
    expected_url = "https://www.xe.com/send-money/send-money-to-canada/"
    try:
        WebDriverWait(driver, 10).until(EC.url_to_be(expected_url))
        print("Send Money to Canada Link Clicked Successfully and Correct Page Loaded")
    except:
        print(f"Send Money to Canada Link Click Failed. Current URL: {driver.current_url}")
footer_link()
time.sleep(2)
driver.back()
time.sleep(2)



# Send Money to Australia Link Click in Footer
def footer_link():
    button = driver.find_element(By.XPATH, Element.send_money_australia)
    assert button.is_displayed(), "Button is visible on the page."
    time.sleep(2)
    button.click()
    driver.implicitly_wait(5)
    expected_url = "https://www.xe.com/send-money/send-money-to-australia/"
    try:
        WebDriverWait(driver, 10).until(EC.url_to_be(expected_url))
        print("Send Money to Australia Link Clicked Successfully and Correct Page Loaded")
    except:
        print(f"Send Money to Australia Link Click Failed. Current URL: {driver.current_url}")
footer_link()
time.sleep(2)
driver.back()
time.sleep(2)



# Send Money to New Zealand Link Click in Footer
def footer_link():
    button = driver.find_element(By.XPATH, Element.send_money_new_zealand)
    assert button.is_displayed(), "Button is visible on the page."
    time.sleep(2)
    button.click()
    driver.implicitly_wait(5)
    expected_url = "https://www.xe.com/send-money/send-money-to-new-zealand/"
    try:
        WebDriverWait(driver, 10).until(EC.url_to_be(expected_url))
        print("Send Money to New Zealand Link Clicked Successfully and Correct Page Loaded")
    except:
        print(f"Send Money to New Zealand Link Click Failed. Current URL: {driver.current_url}")
footer_link()
time.sleep(2)
driver.back()
time.sleep(2)



# Send Money to Wallet Link Click in Footer
def footer_link():
    button = driver.find_element(By.XPATH, Element.send_money_wallet)
    assert button.is_displayed(), "Button is visible on the page."
    time.sleep(2)
    button.click()
    driver.implicitly_wait(5)
    expected_url = "https://www.xe.com/send-money/mobile-wallets/"
    try:
        WebDriverWait(driver, 10).until(EC.url_to_be(expected_url))
        print("Send Money to Wallet Link Clicked Successfully and Correct Page Loaded")
    except:
        print(f"Send Money to Wallet Link Click Failed. Current URL: {driver.current_url}")
footer_link()
time.sleep(2)
driver.back()
time.sleep(2)



# Large Money Transfer Link Click in Footer
def footer_link():
    button = driver.find_element(By.XPATH, Element.large_money_transfer)
    assert button.is_displayed(), "Button is visible on the page."
    time.sleep(2)
    button.click()
    driver.implicitly_wait(5)
    expected_url = "https://www.xe.com/large-money-transfer/"
    try:
        WebDriverWait(driver, 10).until(EC.url_to_be(expected_url))
        print("Large Money Transfer Link Clicked Successfully and Correct Page Loaded")
    except:
        print(f"Large Money Transfer Link Click Failed. Current URL: {driver.current_url}")
footer_link()
time.sleep(2)
driver.back()
time.sleep(2)




# Security Link Click in Footer
def footer_link():
    button = driver.find_element(By.XPATH, Element.security)
    assert button.is_displayed(), "Button is visible on the page."
    time.sleep(2)
    button.click()
    driver.implicitly_wait(5)
    expected_url = "https://www.xe.com/security/"
    try:
        WebDriverWait(driver, 10).until(EC.url_to_be(expected_url))
        print("Security Link Clicked Successfully and Correct Page Loaded")
    except:
        print(f"Security Link Click Failed. Current URL: {driver.current_url}")
footer_link()
time.sleep(2)
driver.back()
time.sleep(2)


# Report Fraud Link Click in Footer
def test_report_fraud_stay():
    try:
        report_fraud_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, Element.report_fraud))
        )
        report_fraud_button.click()
        time.sleep(5)
        stay_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, Element.report_fraud_yes))
        )
        stay_button.click()
        time.sleep(2)
        current_url = driver.current_url
        expected_url = "https://help.xe.com/hc/en-gb/p/contact-details"
        driver.implicitly_wait(5)
        if current_url == expected_url:
            print("Report Fraud Link Clicked Successfully and Correct Page Loaded")
        else:
            print(f"Test failed: User was redirected to {current_url}. Expected: {expected_url}")
    except Exception as e:
        # Print any errors to help with debugging
        print(f"Test failed: {str(e)}")
test_report_fraud_stay()
time.sleep(2)
driver.back()
time.sleep(2)


# Trustpilot Reviews Link Click in Footer
def test_report_fraud_stay():
    try:
        report_fraud_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, Element.trustpilot_reviews))
        )
        report_fraud_button.click()
        time.sleep(2)
        stay_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, Element.trustpilot_yes))
        )
        stay_button.click()
        time.sleep(2)
        current_url = driver.current_url
        expected_url = "https://www.trustpilot.com/review/www.xe.com"
        driver.implicitly_wait(5)
        if current_url == expected_url:
            print("Trustpilot Reviews Link Clicked Successfully and Correct Page Loaded")
        else:
            print(f"Test failed: User was redirected to {current_url}. Expected: {expected_url}")
    except Exception as e:
        # Print any errors to help with debugging
        print(f"Test failed: {str(e)}")
test_report_fraud_stay()
time.sleep(2)
driver.back()
time.sleep(2)


# Business Payments Link Click in Footer
def footer_link():
    button = driver.find_element(By.XPATH, Element.business_payment)
    assert button.is_displayed(), "Button is visible on the page."
    time.sleep(2)
    button.click()
    driver.implicitly_wait(5)
    expected_url = "https://www.xe.com/business/"
    try:
        WebDriverWait(driver, 10).until(EC.url_to_be(expected_url))
        print("Business Payments Link Clicked Successfully and Correct Page Loaded")
    except:
        print(f"Business Payments Click Failed. Current URL: {driver.current_url}")
footer_link()
time.sleep(2)
driver.back()
time.sleep(2)



# International Business Payments Link Click in Footer
def footer_link():
    button = driver.find_element(By.XPATH, Element.international_business_payment)
    assert button.is_displayed(), "Button is visible on the page."
    time.sleep(2)
    button.click()
    driver.implicitly_wait(5)
    expected_url = "https://www.xe.com/business/send-money/"
    try:
        WebDriverWait(driver, 10).until(EC.url_to_be(expected_url))
        print("International Business Payments Link Clicked Successfully and Correct Page Loaded")
    except:
        print(f"International Business Payments Click Failed. Current URL: {driver.current_url}")
footer_link()
time.sleep(2)
driver.back()
time.sleep(2)



# Global Business Payments Link Click in Footer
def footer_link():
    button = driver.find_element(By.XPATH, Element.global_business_payment)
    assert button.is_displayed(), "Button is visible on the page."
    time.sleep(2)
    button.click()
    driver.implicitly_wait(5)
    expected_url = "https://www.xe.com/business/payments/"
    try:
        WebDriverWait(driver, 10).until(EC.url_to_be(expected_url))
        print("Global Business Payments Link Clicked Successfully and Correct Page Loaded")
    except:
        print(f"Global Business Payments Click Failed. Current URL: {driver.current_url}")
footer_link()
time.sleep(2)
driver.back()
time.sleep(2)


# Risk Management Link Click in Footer
def footer_link():
    button = driver.find_element(By.XPATH, Element.risk_management)
    assert button.is_displayed(), "Button is visible on the page."
    time.sleep(2)
    button.click()
    driver.implicitly_wait(5)
    expected_url = "https://www.xe.com/business/fx-risk-management/"
    try:
        WebDriverWait(driver, 10).until(EC.url_to_be(expected_url))
        print("Risk Management Link Clicked Successfully and Correct Page Loaded")
    except:
        print(f"Risk Management Click Failed. Current URL: {driver.current_url}")
footer_link()
time.sleep(2)
driver.back()
time.sleep(2)


# Enterprise Resource Planning Link Click in Footer
def footer_link():
    button = driver.find_element(By.XPATH, Element.enterprise_plan)
    assert button.is_displayed(), "Button is visible on the page."
    time.sleep(2)
    button.click()
    driver.implicitly_wait(5)
    expected_url = "https://www.xe.com/business/erp/"
    try:
        WebDriverWait(driver, 10).until(EC.url_to_be(expected_url))
        print("Enterprise Resource Planning Link Clicked Successfully and Correct Page Loaded")
    except:
        print(f"Enterprise Resource Planning Click Failed. Current URL: {driver.current_url}")
footer_link()
time.sleep(2)
driver.back()
time.sleep(2)


# Currency Data API Integration Link Click in Footer
def footer_link():
    button = driver.find_element(By.XPATH, Element.currency_data_api)
    assert button.is_displayed(), "Button is visible on the page."
    time.sleep(2)
    button.click()
    driver.implicitly_wait(5)
    expected_url = "https://www.xe.com/xecurrencydata/"
    try:
        WebDriverWait(driver, 10).until(EC.url_to_be(expected_url))
        print("Currency Data API Integration Link Clicked Successfully and Correct Page Loaded")
    except:
        print(f"Currency Data API Integration Click Failed. Current URL: {driver.current_url}")
footer_link()
time.sleep(2)
driver.back()
time.sleep(2)



# Affiliate Referral Partner Program Link Click in Footer
def footer_link():
    button = driver.find_element(By.XPATH, Element.affiliated_partner)
    assert button.is_displayed(), "Button is visible on the page."
    time.sleep(2)
    button.click()
    driver.implicitly_wait(5)
    expected_url = "https://www.xe.com/mt/us-business/referral-partner/"
    try:
        WebDriverWait(driver, 10).until(EC.url_to_be(expected_url))
        print("Affiliate Referral Partner Program Link Clicked Successfully and Correct Page Loaded")
    except:
        print(f"Affiliate Referral Partner Program Click Failed. Current URL: {driver.current_url}")
footer_link()
time.sleep(2)
driver.back()
time.sleep(2)


# Mass Payments Link Click in Footer
def footer_link():
    button = driver.find_element(By.XPATH, Element.mass_payment)
    assert button.is_displayed(), "Button is visible on the page."
    time.sleep(2)
    button.click()
    driver.implicitly_wait(5)
    expected_url = "https://www.xe.com/business/mass-payments/"
    try:
        WebDriverWait(driver, 10).until(EC.url_to_be(expected_url))
        print("Mass Payments Link Clicked Successfully and Correct Page Loaded")
    except:
        print(f"Mass Payments Click Failed. Current URL: {driver.current_url}")
footer_link()
time.sleep(2)
driver.back()
time.sleep(2)


# Money Transfer & Currency Apps Link Click in Footer
def footer_link():
    button = driver.find_element(By.XPATH, Element.money_transfer_apps)
    assert button.is_displayed(), "Button is visible on the page."
    time.sleep(2)
    button.click()
    driver.implicitly_wait(5)
    expected_url = "https://www.xe.com/apps/"
    try:
        WebDriverWait(driver, 10).until(EC.url_to_be(expected_url))
        print("Money Transfer & Currency Apps Link Clicked Successfully and Correct Page Loaded")
    except:
        print(f"Money Transfer & Currency Apps Click Failed. Current URL: {driver.current_url}")
footer_link()
time.sleep(2)
driver.back()
time.sleep(2)


# Android Money Transfer Apps Link Click in Footer
def footer_link():
    button = driver.find_element(By.XPATH, Element.android_apps)
    assert button.is_displayed(), "Button is visible on the page."
    time.sleep(2)
    button.click()
    driver.implicitly_wait(5)
    expected_url = "https://www.xe.com/apps/android/"
    try:
        WebDriverWait(driver, 10).until(EC.url_to_be(expected_url))
        print("Android Money Transfer Apps Link Clicked Successfully and Correct Page Loaded")
    except:
        print(f"Android Money Transfer Apps Click Failed. Current URL: {driver.current_url}")
footer_link()
time.sleep(2)
driver.back()
time.sleep(2)



# IOS Money Transfer Apps Link Click in Footer
def footer_link():
    button = driver.find_element(By.XPATH, Element.ios_apps)
    assert button.is_displayed(), "Button is visible on the page."
    time.sleep(2)
    button.click()
    driver.implicitly_wait(5)
    expected_url = "https://www.xe.com/apps/ios/"
    try:
        WebDriverWait(driver, 10).until(EC.url_to_be(expected_url))
        print("IOS Money Transfer Apps Link Clicked Successfully and Correct Page Loaded")
    except:
        print(f"IOS Money Transfer Apps Click Failed. Current URL: {driver.current_url}")
footer_link()
time.sleep(2)
driver.back()
time.sleep(2)


# Blog Link Click in Footer
def footer_link():
    button = driver.find_element(By.XPATH, Element.blog_footer)
    assert button.is_displayed(), "Button is visible on the page."
    time.sleep(2)
    button.click()
    driver.implicitly_wait(5)
    expected_url = "https://www.xe.com/blog/"
    try:
        WebDriverWait(driver, 10).until(EC.url_to_be(expected_url))
        print("Blog Link Clicked Successfully and Correct Page Loaded")
    except:
        print(f"Blog Click Failed. Current URL: {driver.current_url}")
footer_link()
time.sleep(2)
driver.back()
time.sleep(2)


# Currency Converter Link Click in Footer
def footer_link():
    button = driver.find_element(By.XPATH, Element.currency_converter_footer)
    assert button.is_displayed(), "Button is visible on the page."
    time.sleep(2)
    button.click()
    driver.implicitly_wait(5)
    expected_url = "https://www.xe.com/currencyconverter/"
    try:
        WebDriverWait(driver, 10).until(EC.url_to_be(expected_url))
        print("Currency Converter Link Clicked Successfully and Correct Page Loaded")
    except:
        print(f"Currency Converter Click Failed. Current URL: {driver.current_url}")
footer_link()
time.sleep(2)
driver.back()
time.sleep(2)



# Currency Charts Link Click in Footer
def footer_link():
    button = driver.find_element(By.XPATH, Element.currency_charts_footer)
    assert button.is_displayed(), "Button is visible on the page."
    time.sleep(2)
    button.click()
    driver.implicitly_wait(5)
    expected_url = "https://www.xe.com/currencycharts/"
    try:
        WebDriverWait(driver, 10).until(EC.url_to_be(expected_url))
        print("Currency ChartsLink Clicked Successfully and Correct Page Loaded")
    except:
        print(f"Currency Charts Click Failed. Current URL: {driver.current_url}")
footer_link()
time.sleep(2)
driver.back()
time.sleep(2)


# Historical Currency Rates Link Click in Footer
def footer_link():
    button = driver.find_element(By.XPATH, Element.historical_currency_rate_footer)
    assert button.is_displayed(), "Button is visible on the page."
    time.sleep(2)
    button.click()
    driver.implicitly_wait(5)
    expected_url = "https://www.xe.com/currencytables/"
    try:
        WebDriverWait(driver, 10).until(EC.url_to_be(expected_url))
        print("Historical Currency Rates Link Clicked Successfully and Correct Page Loaded")
    except:
        print(f"Historical Currency Rates Click Failed. Current URL: {driver.current_url}")
footer_link()
time.sleep(2)
driver.back()
time.sleep(2)



# Currency Encyclopedia Link Click in Footer
def footer_link():
    button = driver.find_element(By.XPATH, Element.currency_encyclopedia_footer)
    assert button.is_displayed(), "Button is visible on the page."
    time.sleep(2)
    button.click()
    driver.implicitly_wait(5)
    expected_url = "https://www.xe.com/currency/"
    try:
        WebDriverWait(driver, 10).until(EC.url_to_be(expected_url))
        print("Currency Encyclopedia Link Clicked Successfully and Correct Page Loaded")
    except:
        print(f"Currency Encyclopedia Click Failed. Current URL: {driver.current_url}")
footer_link()
time.sleep(2)
driver.back()
time.sleep(2)





# Currency Rate Alerts Link Click in Footer
def footer_link():
    button = driver.find_element(By.XPATH, Element.currency_rate_alert_footer)
    assert button.is_displayed(), "Button is visible on the page."
    time.sleep(2)
    button.click()
    driver.implicitly_wait(5)
    expected_url = "https://www.xe.com/ratealerts/"
    try:
        WebDriverWait(driver, 10).until(EC.url_to_be(expected_url))
        print("Currency Rate Alerts Link Clicked Successfully and Correct Page Loaded")
    except:
        print(f"Currency Rate Alerts Click Failed. Current URL: {driver.current_url}")
footer_link()
time.sleep(2)
driver.back()
time.sleep(2)


# Currency Newsletters Link Click in Footer
def footer_link():
    button = driver.find_element(By.XPATH, Element.currency_newsletter_footer)
    assert button.is_displayed(), "Button is visible on the page."
    time.sleep(2)
    button.click()
    driver.implicitly_wait(5)
    expected_url = "https://www.xe.com/currencyemail/"
    try:
        WebDriverWait(driver, 10).until(EC.url_to_be(expected_url))
        print("Currency Newsletters Link Clicked Successfully and Correct Page Loaded")
    except:
        print(f"Currency Newsletters Click Failed. Current URL: {driver.current_url}")
footer_link()
time.sleep(2)
driver.back()
time.sleep(2)


# Currency Newsletters Link Click in Footer
def footer_link():
    button = driver.find_element(By.XPATH, Element.currency_newsletter_footer)
    assert button.is_displayed(), "Button is visible on the page."
    time.sleep(2)
    button.click()
    driver.implicitly_wait(5)
    expected_url = "https://www.xe.com/currencyemail/"
    try:
        WebDriverWait(driver, 10).until(EC.url_to_be(expected_url))
        print("Currency Newsletters Link Clicked Successfully and Correct Page Loaded")
    except:
        print(f"Currency Newsletters Click Failed. Current URL: {driver.current_url}")
footer_link()
time.sleep(2)
driver.back()
time.sleep(2)



# IBAN Calculator Link Click in Footer
def footer_link():
    button = driver.find_element(By.XPATH, Element.iban_calculator_footer)
    assert button.is_displayed(), "Button is visible on the page."
    time.sleep(2)
    button.click()
    driver.implicitly_wait(5)
    expected_url = "https://www.xe.com/ibancalculator/"
    try:
        WebDriverWait(driver, 10).until(EC.url_to_be(expected_url))
        print("IBAN Calculator Link Clicked Successfully and Correct Page Loaded")
    except:
        print(f"IBAN Calculator Click Failed. Current URL: {driver.current_url}")
footer_link()
time.sleep(2)
driver.back()
time.sleep(2)



# Glossary Link Click in Footer
def footer_link():
    button = driver.find_element(By.XPATH, Element.glossary_footer)
    assert button.is_displayed(), "Button is visible on the page."
    time.sleep(2)
    button.click()
    driver.implicitly_wait(5)
    expected_url = "https://www.xe.com/terms/"
    try:
        WebDriverWait(driver, 10).until(EC.url_to_be(expected_url))
        print("Glossary Link Clicked Successfully and Correct Page Loaded")
    except:
        print(f"Glossary Click Failed. Current URL: {driver.current_url}")
footer_link()
time.sleep(2)
driver.back()
time.sleep(2)




# About us footer Click in Footer
def footer_link():
    button = driver.find_element(By.XPATH, Element.about_us_footer)
    assert button.is_displayed(), "Button is visible on the page."
    time.sleep(2)
    button.click()
    driver.implicitly_wait(5)
    expected_url = "https://www.xe.com/company/"
    try:
        WebDriverWait(driver, 10).until(EC.url_to_be(expected_url))
        print("About us Link Clicked Successfully and Correct Page Loaded")
    except:
        print(f"About us Click Failed. Current URL: {driver.current_url}")
footer_link()
time.sleep(2)
driver.back()
time.sleep(2)


#  Partnerships footer Click in Footer
def footer_link():
    button = driver.find_element(By.XPATH, Element.partnership_footer)
    assert button.is_displayed(), "Button is visible on the page."
    time.sleep(2)
    button.click()
    driver.implicitly_wait(5)
    expected_url = "https://www.xe.com/partnerships/"
    try:
        WebDriverWait(driver, 10).until(EC.url_to_be(expected_url))
        print("Partnerships Link Clicked Successfully and Correct Page Loaded")
    except:
        print(f"Partnerships Click Failed. Current URL: {driver.current_url}")
footer_link()
time.sleep(2)
driver.back()
time.sleep(2)




# Career Link Click in Footer
def test_report_fraud_stay():
    try:
        report_fraud_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, Element.career_footer))
        )
        report_fraud_button.click()
        time.sleep(2)
        stay_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, Element.career_yes))
        )
        stay_button.click()
        time.sleep(2)
        current_url = driver.current_url
        expected_url = "https://apply.workable.com/xe/"
        driver.implicitly_wait(5)
        if current_url == expected_url:
            print("Career Link Clicked Successfully and Correct Page Loaded")
        else:
            print(f"Test failed: User was redirected to {current_url}. Expected: {expected_url}")
    except Exception as e:
        # Print any errors to help with debugging
        print(f"Test failed: {str(e)}")
test_report_fraud_stay()
time.sleep(2)
driver.back()
time.sleep(2)



# Help Center Link Click in Footer
def test_report_fraud_stay():
    try:
        report_fraud_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, Element.help_center_footer))
        )
        report_fraud_button.click()
        time.sleep(2)
        stay_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, Element.help_center_yes))
        )
        stay_button.click()
        time.sleep(2)
        current_url = driver.current_url
        expected_url = "https://help.xe.com/hc/en-gb"
        driver.implicitly_wait(5)
        if current_url == expected_url:
            print("Help Center Link Clicked Successfully and Correct Page Loaded")
        else:
            print(f"Test failed: User was redirected to {current_url}. Expected: {expected_url}")
    except Exception as e:
        # Print any errors to help with debugging
        print(f"Test failed: {str(e)}")
test_report_fraud_stay()
time.sleep(2)
driver.back()
time.sleep(2)



# Site Map footer Click in Footer
def footer_link():
    button = driver.find_element(By.XPATH, Element.sitemap_footer)
    assert button.is_displayed(), "Button is visible on the page."
    time.sleep(2)
    button.click()
    driver.implicitly_wait(5)
    expected_url = "https://www.xe.com/sitemap/"
    try:
        WebDriverWait(driver, 10).until(EC.url_to_be(expected_url))
        print("Site Map Link Clicked Successfully and Correct Page Loaded")
    except:
        print(f"Site Map Click Failed. Current URL: {driver.current_url}")
footer_link()
time.sleep(2)
driver.back()
time.sleep(2)



# Legal footer Click in Footer
def footer_link():
    button = driver.find_element(By.XPATH, Element.legal_footer)
    assert button.is_displayed(), "Button is visible on the page."
    time.sleep(2)
    button.click()
    driver.implicitly_wait(5)
    expected_url = "https://www.xe.com/legal/"
    try:
        WebDriverWait(driver, 10).until(EC.url_to_be(expected_url))
        print("Legal Link Clicked Successfully and Correct Page Loaded")
    except:
        print(f"Legal Click Failed. Current URL: {driver.current_url}")
footer_link()
time.sleep(2)
driver.back()
time.sleep(2)



# Money Transfer footer Click in Footer
def footer_link():
    button = driver.find_element(By.XPATH, Element.money_transfer_footer)
    assert button.is_displayed(), "Button is visible on the page."
    time.sleep(2)
    button.click()
    driver.implicitly_wait(5)
    expected_url = "https://help.xe.com/hc/en-gb/sections/360005694438"
    try:
        WebDriverWait(driver, 10).until(EC.url_to_be(expected_url))
        print("Money Transfer Link Clicked Successfully and Correct Page Loaded")
    except:
        print(f"Money Transfer Click Failed. Current URL: {driver.current_url}")
footer_link()
time.sleep(2)
driver.back()
time.sleep(2)



# File Complaint footer Click in Footer
def footer_link():
    button = driver.find_element(By.XPATH, Element.file_complaint_footer)
    assert button.is_displayed(), "Button is visible on the page."
    time.sleep(2)
    button.click()
    driver.implicitly_wait(5)
    expected_url = "https://help.xe.com/hc/en-gb/sections/13413845846673"
    try:
        WebDriverWait(driver, 10).until(EC.url_to_be(expected_url))
        print("File Complaint Link Clicked Successfully and Correct Page Loaded")
    except:
        print(f"File Complaint Click Failed. Current URL: {driver.current_url}")
footer_link()
time.sleep(2)
driver.back()
time.sleep(2)



# Accessibility footer Click in Footer
def footer_link():
    button = driver.find_element(By.XPATH, Element.accessibility_footer)
    assert button.is_displayed(), "Button is visible on the page."
    time.sleep(2)
    button.click()
    driver.implicitly_wait(5)
    expected_url = "https://help.xe.com/hc/en-gb/articles/13822549001745-Accessibility-Statement"
    try:
        WebDriverWait(driver, 10).until(EC.url_to_be(expected_url))
        print("Accessibility Link Clicked Successfully and Correct Page Loaded")
    except:
        print(f"Accessibility Click Failed. Current URL: {driver.current_url}")
footer_link()
time.sleep(2)
driver.back()
time.sleep(2)


# Facebook Link Open
def test_logo_click():
    try:
        fb_image_link = driver.find_element(By.CSS_SELECTOR, Element.fb_link)
        fb_image_link.click()
        driver.switch_to.window(driver.window_handles[1])
        time.sleep(5)
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        print("Facebook Open and Switched back to the original website page successfully.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
test_logo_click()
time.sleep(3)


# LinkedIn Link Open
def test_logo_click():
    try:
        fb_image_link = driver.find_element(By.CSS_SELECTOR, Element.linkedin_link)
        fb_image_link.click()
        driver.switch_to.window(driver.window_handles[1])
        driver.close()
        time.sleep(5)
        driver.switch_to.window(driver.window_handles[0])
        print("LinkedIn Open and Switched back to the original website page successfully.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
test_logo_click()
time.sleep(3)


# Instagram Link Open
def test_logo_click():
    try:
        insta_image_link = driver.find_element(By.CSS_SELECTOR, Element.insta_logo)
        insta_image_link.click()
        driver.switch_to.window(driver.window_handles[1])
        time.sleep(5)
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        print("Instagram Open and Switched back to the original website page successfully.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
test_logo_click()
time.sleep(3)


driver.quit()