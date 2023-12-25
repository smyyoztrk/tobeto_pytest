from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait #ilgili driverı bekleten yapı
from selenium.webdriver.support import expected_conditions as ec #beklenen koşullar
from selenium.webdriver.common.action_chains import ActionChains
import pytest
class x_ikonu:


    def test_X_ikonu_temizleme(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.saucedemo.com")
        self.driver.maximize_window()    

        usernameInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"user-name")))
    #usernameInput =self.driver.find_element(By.ID,"user-name")
    #inputUsername.send_keys("")
        
        passwordInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"password")))
    #passwordInput = self.driver.find_element(By.ID,"password")
    #inputPassword.send_keys("")

        actions=ActionChains(self.driver)
        actions.send_keys_to_element(usernameInput,"")
        actions.send_keys_to_element(passwordInput,"")
        actions.perform()
        loginButton=self.driver.find_element(By.ID,"login-button")
        loginButton.click()
        
    #errorMessage=self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        x_icon =WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.CSS_SELECTOR,"#login_button_container > div > form > div.error-message-container.error > h3 > button > svg > path")))
        x_ikon_username =WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.CSS_SELECTOR,"#login_button_container > div > form > div:nth-child(1) > svg")))
        x_ikonu_password = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.CSS_SELECTOR,"#login_button_container > div > form > div:nth-child(2) > svg")))
        
        sleep(2)
        x_icon.click()
    #login_button_container > div > form > div:nth-child(1) > svg > path

        sleep(2)
        try:
            x_icon.is_displayed()
            x_ikon_username.is_displayed()
            x_ikonu_password.is_displayed()
            testResult = False
            assert testResult == True
           
        except:
            testResult= True
        
            assert testResult == True

    

    def test_eslesmeyen_kullanici(self):

        self.driver = webdriver.Chrome()
        self.driver.get("https://www.saucedemo.com")
        self.driver.maximize_window()    

        usernameInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"user-name")))
        passwordInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"password")))
        actions=ActionChains(self.driver)
        actions.send_keys_to_element(usernameInput,"performance_glitch_user")
        actions.send_keys_to_element(passwordInput,"1")
        actions.perform()

        loginButton=self.driver.find_element(By.ID,"login-button")
        loginButton.click()

        

        
        
        errorMessage = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")))
        testResult = errorMessage.text == "Epic sadface: Username and password do not match any user in this service"
        print(testResult)
        #login_button_container > div > form > div.error-message-container.error > h3 > button > svg > path

    def sepete_urun_ekleme(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.saucedemo.com")
        self.driver.maximize_window()
        
        usernameInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"user-name")))
        passwordInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"password")))
        actions=ActionChains(self.driver)
        actions.send_keys_to_element(usernameInput,"standard_user")
        actions.send_keys_to_element(passwordInput,"secret_sauce")
        actions.perform()

        loginButton=self.driver.find_element(By.ID,"login-button")
        loginButton.click()
        
        addToCard = WebDriverWait(self.driver,5).until(ec.visibility_of_all_elements_located((By.XPATH,"//div[@class='inventory_item']//button")))
        #addToCard = WebDriverWait(self.driver,5).until(ec.visibility_of_all_elements_located((By.CLASS_NAME,"btn btn_primary btn_small btn_inventory"))) #ana sayfadaki tüm ürünleri bul
        #addToCard = WebDriverWait(self.driver,5).until(ec.visibility_of_all_elements_located((By.XPATH,"/html/body/div/div/div/div[2]/div/div/div/div/div[2]/div[2]/button"))) #ana sayfadaki tüm ürünleri bul
        print(f"bulunan element:{len(addToCard)}")

        for i in range(len(addToCard)): # ana sayfadaki ürünleri sepete ekle
            addToCard[i].click()

        sepet = self.driver.find_element(By.XPATH,"//*[@id='shopping_cart_container']/a").click() #sepet butonunu bul ve tıkla
        sepetteki_urunler = self.driver.find_elements(By.CLASS_NAME,"cart_item") # sepetteki ürünleri bul
        print(f"septteki ürünler:{len(sepetteki_urunler)} adet")
        
    def sepetten_urun_silme(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.saucedemo.com")
        self.driver.maximize_window()
        
        usernameInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"user-name")))
        passwordInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"password")))
        actions=ActionChains(self.driver)
        actions.send_keys_to_element(usernameInput,"standard_user")
        actions.send_keys_to_element(passwordInput,"secret_sauce")
        actions.perform()

        loginButton=self.driver.find_element(By.ID,"login-button")
        loginButton.click()
        addToCard = WebDriverWait(self.driver,5).until(ec.visibility_of_all_elements_located((By.XPATH,"/html/body/div/div/div/div[2]/div/div/div/div/div[2]/div[2]/button"))) #ana sayfadaki tüm ürünleri bul
        print(f"bulunan element:{len(addToCard)}")

        for i in range(len(addToCard)): # ana sayfadaki ürünleri sepete ekle
            addToCard[i].click()

        sepet = self.driver.find_element(By.XPATH,"//*[@id='shopping_cart_container']/a").click() #sepet butonunu bul ve tıkla
        sepetteki_urunler = self.driver.find_elements(By.CLASS_NAME,"cart_item") # sepetteki ürünleri bul
        print(f"septteki ürünler:{len(sepetteki_urunler)} adet")

        remove = WebDriverWait(self.driver,5).until(ec.visibility_of_all_elements_located((By.XPATH,"/html/body/div/div/div/div[2]/div/div[1]/div/div[2]/div[2]/button")))
        
        for i in range(3):
            sleep(2)
            remove[i].click()
            try:
                remove[i].is_displayed()
                testResult = False
                break
            except:
                testResult = True
                continue
            
        #assert testResult == True
        print(f"sepette ürün kalmadı:{testResult}")
    
        
        

testclass = x_ikonu()
#testclass.test_X_ikonu_temizleme()
#testclass.test_eslesmeyen_kullanici()    
testclass.sepete_urun_ekleme() 
#testclass.sepetten_urun_silme()




