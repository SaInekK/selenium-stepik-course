# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 17:35:32 2021

@author: User
"""

import time
from selenium import webdriver
from math import log, sin

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/redirect_accept.html")


try:
    browser.find_element_by_css_selector('.btn.btn-primary').click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    # alert = browser.switch_to.alert
    # alert.accept()
    x = browser.find_element_by_css_selector('#input_value').text
    browser.find_element_by_css_selector('#answer') \
        .send_keys(str(log(abs(12 * sin(int(x))))))
    browser.find_element_by_css_selector('.btn.btn-primary').click()
    
    alert = browser.switch_to.alert
    answer = alert.text.split()[-1]
    print(answer)
    # for selector in ['[for="robotCheckbox"]', '[for="robotsRule"]', '.btn']:
    #     browser.find_element_by_css_selector(selector).click()

finally:
    time.sleep(10)
    browser.quit()