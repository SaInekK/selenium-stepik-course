# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 22:02:07 2021

@author: User
"""
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
browser = webdriver.Chrome()

# type(browser)
# browser.get('http://inventwithpython.com')

# try:
#     elem = browser.find_element_by_css_selector('.col-sm-12 img')
#     print(f'Found element <{elem.tag_name}> with expected class name')
#     elem.click()
    
# except:
#     print('Element not found')




# browser.get('http://gmail.com')

# emailElem = browser.find_element_by_css_selector('[type=email]')
# emailElem.send_keys('blablamail@gmail.com')
# emailElem.submit()
# emailElem = browser.find_element_by_id('Passwd')
# emailElem.send_keys('12345')
# emailElem.submit()

browser.get('http://inventwithpython.com')
#browser.get('http://nostarch.com')
htmlElem = browser.find_element_by_css_selector('body')
time.sleep(3)
htmlElem.send_keys(Keys.END)
time.sleep(3)
htmlElem.send_keys(Keys.HOME)