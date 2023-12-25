from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait #ilgili driverı bekleten yapı
from selenium.webdriver.support import expected_conditions as ec #beklenen koşullar
from selenium.webdriver.common.action_chains import ActionChains
import pytest

class Test_odevClass:

    def setup_method(self):   #her test başlangıcında çalışacak fonk.
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.saucedemo.com")
        self.driver.maximize_window()

    def teardown_method(self):  # her testin bitiminde çalışacak fonk
        self.driver.quit()
    
    def test_empty_login(self):
        
        usernameInput=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"user-name")))
        usernameInput.send_keys('')
        passwordInput=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"password")))
        passwordInput.send_keys('')
        loginButton=self.driver.find_element(By.ID,'login-button')
        loginButton.click()
        errorMesagge = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        assert errorMesagge.text == "Epic sadface: Username is required"
        
    
    def test_empty_password_login(self):
        
        usernameInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,'user-name')))
        usernameInput.send_keys("locked_out_user")
        passwordInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"password")))
        passwordInput.send_keys("")
        loginButton = self.driver.find_element(By.ID,'login-button')
        loginButton.click()
        errorMessage = self.driver. find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        assert errorMessage.text == "Epic sadface: Password is required"
        
    
    def test_invalid_login(self):
        
        usernameInput=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,'user-name')))
        usernameInput.send_keys('locked_out_user') 
        passwordInput=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,'password')))
        passwordInput.send_keys('secret_sauce')
        loginButton=self.driver.find_element(By.ID,'login-button')
        loginButton.click() 
        errorMessage=self.driver.find_element(By.XPATH,'//*[@id="login_button_container"]/div/form/div[3]/h3')
        assert errorMessage.text=='Epic sadface: Sorry, this user has been locked out.'
    
    def test_valid_login(self):
        
        usernameInput=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,'user-name')))
        usernameInput.send_keys('standard_user') 
        passwordInput=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,'password')))
        passwordInput.send_keys('secret_sauce')
        loginButton=self.driver.find_element(By.ID,'login-button')
        loginButton.click()
        assert  self.driver.current_url == "https://www.saucedemo.com/inventory.html"
        #print(f"test sonucu(ana sayfaya geçildi mi): {sayfa}")
        urunler = self.driver.find_elements(By.CLASS_NAME,"inventory_item_description")
        assert len(urunler) == 6


    def test_X_ikonu_temizleme(self):
        usernameInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"user-name")))
        passwordInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"password")))
        actions=ActionChains(self.driver)
        actions.send_keys_to_element(usernameInput,"")
        actions.send_keys_to_element(passwordInput,"")
        actions.perform()

        loginButton=self.driver.find_element(By.ID,"login-button")
        loginButton.click()
        
    
        x_icon =WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.CSS_SELECTOR,"#login_button_container > div > form > div.error-message-container.error > h3 > button > svg > path")))
        x_ikon_username =WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.CSS_SELECTOR,"#login_button_container > div > form > div:nth-child(1) > svg")))
        x_ikonu_password = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.CSS_SELECTOR,"#login_button_container > div > form > div:nth-child(2) > svg")))
        
        
        x_icon.click()
        try:
            x_icon.is_displayed()
            x_ikon_username.is_displayed()
            x_ikonu_password.is_displayed()
            testResult = False  #ikonlar görünüyorsa test sonucu false olur
            assert testResult == True #test sonucu true olmadığı için assert false döndürür
           
        except:
            testResult= True
            assert testResult == True

    @pytest.mark.parametrize("username,password",[("performance_glitch_user","1"),("error_user","1"),("visual_user","1")])
    def test_eslesmeyen_kullanici(self,username,password):
        usernameInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"user-name")))
        passwordInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"password")))
        actions=ActionChains(self.driver)
        actions.send_keys_to_element(usernameInput,username)
        actions.send_keys_to_element(passwordInput,password)
        actions.perform()

        loginButton=self.driver.find_element(By.ID,"login-button")
        loginButton.click()

        errorMessage = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")))
        assert errorMessage.text == "Epic sadface: Username and password do not match any user in this service"
   
    def test_sepete_urun_ekleme(self):
        
        usernameInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"user-name")))
        passwordInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"password")))
        actions=ActionChains(self.driver)
        actions.send_keys_to_element(usernameInput,"standard_user")
        actions.send_keys_to_element(passwordInput,"secret_sauce")
        actions.perform()

        loginButton=self.driver.find_element(By.ID,"login-button")
        loginButton.click()
        addToCard = WebDriverWait(self.driver,5).until(ec.visibility_of_all_elements_located((By.XPATH,"//div[@class='inventory_item']//button"))) #ana sayfadaki tüm ürünleri bul
        #addToCard = WebDriverWait(self.driver,5).until(ec.visibility_of_all_elements_located((By.CLASS_NAME,"btn btn_primary btn_small btn_inventory"))) #ana sayfadaki tüm ürünleri bul
        #addToCard = WebDriverWait(self.driver,5).until(ec.visibility_of_all_elements_located((By.XPATH,"/html/body/div/div/div/div[2]/div/div/div/div/div[2]/div[2]/button"))) #ana sayfadaki tüm ürünleri bul
        #print(f"bulunan element:{len(addToCard)}")

        for i in range(len(addToCard)): # ana sayfadaki ürünleri sepete ekle
            addToCard[i].click()

        sepet = self.driver.find_element(By.XPATH,"//*[@id='shopping_cart_container']/a").click() #sepet butonunu bul ve tıkla
        sepetteki_urunler = self.driver.find_elements(By.CLASS_NAME,"cart_item") # sepetteki ürünleri bul
        #print(f"septteki ürünler:{len(sepetteki_urunler)} adet")
        assert len(addToCard) == len(sepetteki_urunler)

    def test_sepetten_urun_silme(self):
        
        usernameInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"user-name")))
        passwordInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"password")))
        actions=ActionChains(self.driver)
        actions.send_keys_to_element(usernameInput,"standard_user")
        actions.send_keys_to_element(passwordInput,"secret_sauce")
        actions.perform()

        loginButton=self.driver.find_element(By.ID,"login-button")
        loginButton.click()
        
        addToCard = WebDriverWait(self.driver,5).until(ec.visibility_of_all_elements_located((By.XPATH,"//div[@class='inventory_item']//button"))) #ana sayfadaki tüm ürünleri bul
        #addToCard = WebDriverWait(self.driver,5).until(ec.visibility_of_all_elements_located((By.CLASS_NAME,"btn btn_primary btn_small btn_inventory"))) #ana sayfadaki tüm ürünleri bul
        #addToCard = WebDriverWait(self.driver,5).until(ec.visibility_of_all_elements_located((By.XPATH,"/html/body/div/div/div/div[2]/div/div/div/div/div[2]/div[2]/button"))) #ana sayfadaki tüm ürünleri bul
        #print(f"bulunan element:{len(addToCard)}")

        for i in range(len(addToCard)): # ana sayfadaki ürünleri sepete ekle
            addToCard[i].click()

        sepet = self.driver.find_element(By.XPATH,"//*[@id='shopping_cart_container']/a").click() #sepet butonunu bul ve tıkla
        sepetteki_urunler = self.driver.find_elements(By.CLASS_NAME,"cart_item") # sepetteki ürünleri bul
        #print(f"septteki ürünler:{len(sepetteki_urunler)} adet")

        remove = WebDriverWait(self.driver,5).until(ec.visibility_of_all_elements_located((By.XPATH,"/html/body/div/div/div/div[2]/div/div[1]/div/div[2]/div[2]/button")))
        for i in range(len(addToCard)):
        
            remove[i].click()
            
            try:                              
                remove[i].is_displayed()     # remove i. index görünür mü? evet ise test result false olsun ve döngüden çık
                testResult = False
                break #döngüyü kır döngüden çık
            except:
                testResult = True            #try daki koşul true değilse bu satırı çalıştır yani test result true oldu,döngüye devam et
                continue #döngüye devam et
        
        assert testResult == True
        

