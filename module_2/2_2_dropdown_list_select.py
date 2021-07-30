# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 15:42:25 2021

@author: User
"""

from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select


try:
    link = 'http://suninjuly.github.io/selects1.html'
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    smth = 'some_value'
    # browser.find_element_by_css_selector('.first_block .form-group.first_class .form-control').send_keys(smth)
    s = int(browser.find_element_by_css_selector('#num1').text) + \
        int(browser.find_element_by_css_selector('#num2').text)
        
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str(s))
    browser.find_element_by_css_selector('.btn.btn-default').click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()