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

    def test_Sucses_Register(self): 
        
        self.browser.get("https://www.sepulsa.com/")
        time.sleep(3)
        self.browser.find_element(By.ID,"Path_27885").click() 
        time.sleep(3)
        self.browser.find_element(By.ID,"Steam Game CD Keys").click() 
        time.sleep(3)
        self.browser.find_element(By.ID,"phone_number").send_keys("085725164649") 
        time.sleep(3)

        self.browser.find_element(By.ID,"Steam Game CD Keys - Dark Souls II: Scholar of The First Sin").click()
        time.sleep(3)
        
        self.browser.find_element(By.ID,"guest_email").send_keys("heruusus@gmail.com")
        time.sleep(3)

        result = self.browser.find_element(By.ID,"checkbox MANDIRI Virtual Account").is_selected()
        if result:
            print('Checkbox already selected')
        else:
            self.browser.find_element(By.ID,"checkbox MANDIRI Virtual Account").click()
            print('Checkbox selected')
        time.sleep(3)

        self.browser.find_element(By.XPATH," /html/body/div/div/div[5]/div/button/span[1]").click()
        time.sleep(3)
       

if __name__ == "__main__": 
    unittest.main()




