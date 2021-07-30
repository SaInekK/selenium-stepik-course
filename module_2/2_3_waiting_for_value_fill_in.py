# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 20:55:34 2021

@author: User
"""

import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from math import log, sin

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")


try:
    button = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
        )
    browser.find_element_by_css_selector('.btn.btn-primary').click()
    x = browser.find_element_by_css_selector('#input_value').text
    browser.find_element_by_css_selector('#answer') \
        .send_keys(str(log(abs(12 * sin(int(x))))))
    browser.find_element_by_css_selector('#solve').click()
    browser.implicitly_wait(5)
    alert = browser.switch_to.alert
    answer = alert.text.split()[-1]
    print(answer)

    
    # x = browser.find_element_by_css_selector('#input_value').text
    # browser.find_element_by_css_selector('#answer') \
    #     .send_keys(str(log(abs(12 * sin(int(x))))))
    # browser.find_element_by_css_selector('.btn.btn-primary').click()
    
    # alert = browser.switch_to.alert
    # answer = alert.text.split()[-1]
    # print(answer)
    # for selector in ['[for="robotCheckbox"]', '[for="robotsRule"]', '.btn']:
    #     browser.find_element_by_css_selector(selector).click()

finally:
    time.sleep(10)
    browser.quit()