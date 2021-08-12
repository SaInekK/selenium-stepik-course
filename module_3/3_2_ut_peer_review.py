# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 12:38:45 2021

@author: User
"""

from selenium import webdriver
import time
import unittest

class TestAbs(unittest.TestCase):
    def test_reg1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)
    
        # Ваш код, который заполняет обязательные поля
        smth = 'some_value'
        browser.find_element_by_css_selector('.first_block .form-group.first_class .form-control').send_keys(smth)
        browser.find_element_by_css_selector('.first_block .form-group.second_class .form-control').send_keys(smth)
        browser.find_element_by_css_selector('.first_block .form-group.third_class .form-control').send_keys(smth)
        
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
    
        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        # time.sleep(5)
    
        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
    
        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        text =  "Congratulations! You have successfully registered!"
        self.assertEqual(welcome_text, text, "registration is failed")
        browser.quit()
        
    def test_reg2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)
    
        # Ваш код, который заполняет обязательные поля
        smth = 'some_value'
        browser.find_element_by_css_selector('.first_block .form-group.first_class .form-control').send_keys(smth)
        browser.find_element_by_css_selector('.first_block .form-group.second_class .form-control').send_keys(smth)
        browser.find_element_by_css_selector('.first_block .form-group.third_class .form-control').send_keys(smth)
        
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
    
        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        # time.sleep(5)
    
        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
    
        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        text =  "Congratulations! You have successfully registered!"
        self.assertEqual(welcome_text, text, "registration is failed")
        browser.quit()

    

if __name__ == "__main__":
    unittest.main()
    


