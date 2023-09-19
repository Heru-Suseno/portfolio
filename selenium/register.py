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
        self.browser.find_element(By.CLASS_NAME,"MuiButton-label").click() 
        time.sleep(3)
        self.browser.find_element(By.ID,"redirect_register").click() 
        time.sleep(3)
        self.browser.find_element(By.ID,"name").send_keys("heruuu")
        time.sleep(3)
        self.browser.find_element(By.ID,"email").send_keys("heru@gmail.com")
        time.sleep(3)
        self.browser.find_element(By.ID,"phone").send_keys("0895327847800")
        time.sleep(3)
        self.browser.find_element(By.ID,"password").send_keys("12345")
        time.sleep(3)
        result = self.browser.find_element(By.ID,"checkbox").is_selected()
        if result:
            print('Checkbox already selected')
        else:
            self.browser.find_element(By.ID,"checkbox").click()
            print('Checkbox selected')
        time.sleep(3)
        self.browser.find_element(By.XPATH,"/html/body/div/div[2]/div/form/div[6]").click()
        time.sleep(3)

    def test_gagal_Register(self): 
        
        self.browser.get("https://www.sepulsa.com/")
        time.sleep(3)
        self.browser.find_element(By.CLASS_NAME,"MuiButton-label").click() 
        time.sleep(3)
        self.browser.find_element(By.ID,"redirect_register").click() 
        time.sleep(3)
        self.browser.find_element(By.ID,"name").send_keys(" ")
        time.sleep(3)
        self.browser.find_element(By.ID,"email").send_keys("heru@gmail.com")
        time.sleep(3)
        self.browser.find_element(By.ID,"phone").send_keys("0895327847800")
        time.sleep(3)
        self.browser.find_element(By.ID,"password").send_keys("12345")
        time.sleep(3)
        result = self.browser.find_element(By.ID,"checkbox").is_selected()
        if result:
            print('Checkbox already selected')
        else:
            self.browser.find_element(By.ID,"checkbox").click()
            print('Checkbox selected')
        time.sleep(3)
        self.browser.find_element(By.XPATH,"/html/body/div/div[2]/div/form/div[6]").click()
        time.sleep(3)

if __name__ == "__main__": 
    unittest.main()


