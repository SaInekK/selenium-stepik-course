# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 18:15:39 2021

@author: User
"""
import os


from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select


try:
    link = 'http://suninjuly.github.io/file_input.html'
    browser = webdriver.Chrome()
    browser.get(link)
    smth = 'some_value'
    
    for e in browser.find_elements_by_css_selector('.form-control'):
        e.send_keys(smth)
    
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'doc.txt')           # добавляем к этому пути имя файла 
    browser.find_element_by_css_selector('#file').send_keys(file_path)
        
    # select = Select(browser.find_element_by_tag_name("select"))
    # select.select_by_value(str(s))
    browser.find_element_by_css_selector('.btn.btn-primary').click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
    
# print(os.path.abspath(__file__))
# print(os.path.abspath(os.path.dirname(__file__)))