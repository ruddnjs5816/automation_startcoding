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
# driver.maximize_window #화면 최대화 

# 아이디 입력창 element = 태그 
# id.send_keys("ruddnjs5816")
id = driver.find_element(By.CSS_SELECTOR, "#id")
id.click()
pyperclip.copy("ruddnjs5816")
pyautogui.hotkey("ctrl", "v")
# time.sleep(2)

# 비밀번호 입력창 
# pw.send_keys("qkrruddnjs@1724")
pw = driver.find_element(By.CSS_SELECTOR, "#pw")
pw.click()
pyperclip.copy("qkrruddnjs@1724")
pyautogui.hotkey("ctrl", "v")
# time.sleep(2)

# 로그인 버튼 
driver.find_element(By.CSS_SELECTOR, "#log\.login").click() 

# 메일 아이콘 클릭
mail = driver.find_element(By.CSS_SELECTOR, "#shortcutArea > ul > li:nth-child(1) > a > span.service_icon.type_mail")
mail.click()


# 메일 쓰기 클릭
time.sleep(5)
driver.find_element(By.CSS_SELECTOR, "#root > div > nav > div > div.lnb_header > div.lnb_task > a.item.button_write").click()

