# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 18:04:39 2021

@author: User
"""

import math
import time
from selenium import webdriver

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/find_xpath_form")

try:

    quiz_list = ['alex', 'lebovski', 'spb', 'russia']
    for i, e in enumerate(browser.find_elements_by_css_selector \
                       ('input[type=text]:nth-child(2)')):
        e.send_keys(quiz_list[i])
    button = browser.find_element_by_xpath("//button[text()='Submit']")
    button.click()


except Exception as error:
    print(f'Произошла ошибка, вот её трэйсбэк: {error}')
    
finally:
    time.sleep(20)
    browser.close()
    time.sleep(20)
    browser.quit()