# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 19:26:09 2021

@author: User
"""

import time
from selenium import webdriver
# from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/huge_form.html")

try:
    ans = 'smth'
    for e in browser.find_elements_by_css_selector('input[type=text]'):
        e.send_keys(ans)
    button = browser.find_element_by_css_selector("button[type=submit]")
    button.click()



except Exception as error:
    print(f'Произошла ошибка, вот её трэйсбэк: {error}')
    
finally:
    time.sleep(10)
    browser.close()
    browser.quit()