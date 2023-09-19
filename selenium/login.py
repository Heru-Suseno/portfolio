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

    def test_Gagal_login_dengan_email_tidak_terdaftar(self): 
        self.browser.get("https://www.sepulsa.com/")
        time.sleep(3)
        self.browser.find_element(By.CLASS_NAME,"MuiButton-label").click() 
        time.sleep(3)
        self.browser.find_element(By.XPATH,"/html/body/div/div/div[2]/form/div[1]/div/label/span/div[2]/input").send_keys("heru@gmail.com") 
        time.sleep(2)
        self.browser.find_element(By.XPATH,"/html/body/div/div/div[2]/form/div[2]/div/label/span/div[2]/input").send_keys("heruuu") 
        time.sleep(2)
        self.browser.find_element(By.CLASS_NAME,"signup-button").click() 
        time.sleep(3)
        alert = self.browser.find_element(By.ID, "alert_description").text
        time.sleep(2)
        self.assertIn(alert,"Coba ingat-ingat lagi alamat e-mail/ nomor handphone dan password kamu. Masih ada yang salah nih.")

    def test_Gagal_login_dengan_email_password_kosong(self): 
        self.browser.get("https://www.sepulsa.com/")
        time.sleep(3)
        self.browser.find_element(By.CLASS_NAME,"MuiButton-label").click() 
        time.sleep(3)
        self.browser.find_element(By.XPATH,"/html/body/div/div/div[2]/form/div[1]/div/label/span/div[2]/input").send_keys(" ") 
        time.sleep(2)
        self.browser.find_element(By.XPATH,"/html/body/div/div/div[2]/form/div[2]/div/label/span/div[2]/input").send_keys(" ") 
        time.sleep(2)
        self.browser.find_element(By.CLASS_NAME,"signup-button").click() 
        time.sleep(3)
        alert = self.browser.find_element(By.ID, "alert_description").text
        time.sleep(2)
        self.assertIn(alert,"Coba ingat-ingat lagi alamat e-mail/ nomor handphone dan password kamu. Masih ada yang salah nih.")
   
if __name__ == "__main__": 
    unittest.main()


