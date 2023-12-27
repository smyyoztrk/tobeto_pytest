# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from time import sleep
import openpyxl
from constants import globalConstants as c

class Testxikonutemizleme():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_xikonutemizleme(self):
    self.driver = webdriver.Chrome()
    self.driver.get(c.BASE_URL)
    self.driver.set_window_size(1382, 744)
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"login-button\"]").click()
    element = self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"login-button\"]")
    # actions = ActionChains(self.driver)
    # actions.move_to_element(element).perform()
    # element = self.driver.find_element(By.CSS_SELECTOR, "body")
    # actions = ActionChains(self.driver)
    # actions.move_to_element(element, 0, 0).perform()
    self.driver.find_element(By.CSS_SELECTOR, ".fa-times > path").click()
   
    elements = self.driver.find_elements(By.CSS_SELECTOR, c.X_IKON_USERNAME_CSSSELECTOR)
    #elements = self.driver.find_elements(By.CSS_SELECTOR, ".form_group:nth-child(1) > .svg-inline--fa")
    assert len(elements) == 0
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".form_group:nth-child(2) > .svg-inline--fa")
    assert len(elements) == 0
    
    self.driver.close()



classname = Testxikonutemizleme()
#classname.test_xikonutemizleme()