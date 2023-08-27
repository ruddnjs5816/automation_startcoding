from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time

##유지코드
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)



driver.get("https://www.naver.com")