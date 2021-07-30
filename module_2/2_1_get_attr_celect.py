# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 13:42:55 2021

@author: User
"""

from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    # link = "http://suninjuly.github.io/math.html"
    link = 'http://suninjuly.github.io/get_attribute.html'
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    smth = 'some_value'
    # browser.find_element_by_css_selector('.first_block .form-group.first_class .form-control').send_keys(smth)
    # browser.find_element_by_css_selector('.first_block .form-group.second_class .form-control').send_keys(smth)
    # browser.find_element_by_css_selector('.first_block .form-group.third_class .form-control').send_keys(smth)
    # x = int(browser.find_element_by_css_selector('#input_value').text)
    x = int(browser.find_element_by_css_selector('#treasure').get_attribute('valuex'))
    browser.find_element_by_css_selector('#answer').send_keys(calc(x))
    browser.find_element_by_css_selector('#robotCheckbox').click()
    browser.find_element_by_css_selector('#robotsRule').click()
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector(".btn.btn-default")
    button.click()
    
    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(5)

    # # находим элемент, содержащий текст
    # welcome_text_elt = browser.find_element_by_tag_name("h1")
    # # записываем в переменную welcome_text текст из элемента welcome_text_elt
    # welcome_text = welcome_text_elt.text

    # # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    # assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()