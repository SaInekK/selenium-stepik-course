# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 17:15:40 2021

@author: User
"""
import time
from selenium import webdriver
# from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/simple_form_find_task.html")

try:
    quiz_list = ['alex', 'lebovski', 'spb', 'russia']
    for i, e in enumerate(browser.find_elements_by_css_selector \
                       ('input[type=text]:nth-child(2)')):
        e.send_keys(quiz_list[i])
    button = browser.find_element_by_id("submit_button")
    button.click()



except Exception as error:
    print(f'Произошла ошибка, вот её трэйсбэк: {error}')
    
finally:
    browser.close()
    time.sleep(2)
    browser.quit()
