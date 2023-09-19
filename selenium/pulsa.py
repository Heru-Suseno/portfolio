import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class TestLogin(unittest.TestCase):

    def setUp(self): 
        s=Service(ChromeDriverManager().install())
        self.browser = webdriver.Chrome(service=s)

    def test_Register(self): 
        
        self.browser.get("https://www.sepulsa.com/")
        time.sleep(3)
        self.browser.find_element(By.ID,"Pulsa").click() 
        time.sleep(3)
        self.browser.find_element(By.ID,"phone_number").send_keys("085725164649")
        time.sleep(3)
        self.browser.find_element(By.ID,"Indosat Rp5.000").click() 
        time.sleep(3)
        self.browser.find_element(By.ID,"guest_email").send_keys("heruuss@gmail.com")
        time.sleep(3)

        result = self.browser.find_element(By.ID,"checkbox Gopay").is_selected()
        if result:
            print('Checkbox already selected')
        else:
            self.browser.find_element(By.ID,"checkbox Gopay").click()
            print('Checkbox selected')
        time.sleep(3)

        self.browser.find_element(By.ID,"submit_payment").click() 
        time.sleep(4)
        self.browser.find_element(By.ID,"react").click() 
        time.sleep(4)

if __name__ == "__main__": 
    unittest.main()
  