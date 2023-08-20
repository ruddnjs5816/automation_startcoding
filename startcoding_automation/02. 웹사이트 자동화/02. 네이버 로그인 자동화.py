from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time
import pyperclip
import pyautogui


## 크롬 창 유지코드
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)


driver.get("https://nid.naver.com/nidlogin.login?mode=form&url=https://www.naver.com/")
driver.maximize_window #화면 최대화 

# 아이디 입력창 element = 태그 
# id.send_keys("ruddnjs5816")
id = driver.find_element(By.CSS_SELECTOR, "#id")
id.click()
pyperclip.copy("ruddnjs5816")
pyautogui.hotkey("ctrl", "v")
time.sleep(2)

# 비밀번호 입력창 
# pw.send_keys("qkrruddnjs@1724")
pw = driver.find_element(By.CSS_SELECTOR, "#pw")
pw.click()
pyperclip.copy("qkrruddnjs@1724")
pyautogui.hotkey("ctrl", "v")
time.sleep(2)

# 로그인 버튼 
driver.find_element(By.CSS_SELECTOR, "#log\.login").click() 