# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 17:33:20 2021

@author: User
"""
import time
from selenium import webdriver
from math import log, sin
try:
    browser = webdriver.Chrome()
    link = "https://SunInJuly.github.io/execute_script.html"
    browser.get(link)
    x = browser.find_element_by_css_selector('#input_value').text
    button = browser.find_element_by_tag_name("button")
    # browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    browser.execute_script("window.scrollBy(0, 100);")
    for selector in ['#robotCheckbox', '#robotsRule']:
        browser.find_element_by_css_selector(selector).click()
    browser.find_element_by_id('answer').send_keys(str(log(abs(12 * sin(int(x))))))
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()