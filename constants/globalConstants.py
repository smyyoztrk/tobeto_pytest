BASE_URL = "https://www.saucedemo.com"
INPUTLAR_XLSX = "data/inputlar.xlsx"
USERNAME_ID = "user-name"
PASSWORD_ID = "password"
LOGIN_BUTTON_ID ="login-button"
ERROR_MESSAGE_XPATH = "//*[@id='login_button_container']/div/form/div[3]/h3"
URUNLER_CLASSNAME = "inventory_item_description"
X_IKON_CSSSELECTOR = "#login_button_container > div > form > div.error-message-container.error > h3 > button > svg > path"
X_IKON_USERNAME_CSSSELECTOR = "#login_button_container > div > form > div:nth-child(1) > svg"
X_IKON_PASSWORD_CSSSELECTOR = "#login_button_container > div > form > div:nth-child(2) > svg"
ADDTOCARD_XPATH = "//div[@class='inventory_item']//button"
SEPET_XPATH = "//*[@id='shopping_cart_container']/a"
SEPETTEKİ_URUNLER_CLASSNAME = "cart_item"
REMOVE_XPATH = "/html/body/div/div/div/div[2]/div/div[1]/div/div[2]/div[2]/button"

EMPYT_LOGIN_MESSAGE = "Epic sadface: Username is required"
EMPYTY_PASSWORD_MESSAGE = "Epic sadface: Password is required"
INVALİD_LOGIN_MESSAGE = 'Epic sadface: Sorry, this user has been locked out.'
ESLESMEYEN_KULLANİCİ_MESSAGE = "Epic sadface: Username and password do not match any user in this service"

CURRENT_URL_ANASAYFA = "https://www.saucedemo.com/inventory.html"