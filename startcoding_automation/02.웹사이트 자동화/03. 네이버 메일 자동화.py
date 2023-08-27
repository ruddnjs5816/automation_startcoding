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
time.sleep(2)

# 메일 아이콘 클릭
# mail = driver.find_element(By.CSS_SELECTOR, "#shortcutArea > ul > li:nth-child(1) > a > span.service_icon.type_mail")
# mail.click()
driver.get("https://mail.naver.com/v2/folders/0/all")
time.sleep(2)


# 메일 쓰기 버튼 클릭
driver.find_element(By.CSS_SELECTOR, "#root > div > nav > div > div.lnb_header > div.lnb_task > a.item.button_write").click()
time.sleep(2)

# 받는 사람
driver.find_element(By.CSS_SELECTOR, "#recipient_input_element").send_keys("ruddnjs5816@naver.com")
time.sleep(2)

# 제목
driver.find_element(By.CSS_SELECTOR, "#subject_title").send_keys("자동화한 메일")
time.sleep(2)

# 내용
# iframe 페이지안에 또 다른 페이지 
# iframe 안으로 들어가기
iframe = driver.find_element(By.CSS_SELECTOR,"#content > div.contents_area > div > div.editor_area > div > div.editor_body > iframe")
driver.switch_to.frame(iframe)

driver.find_element(By.CSS_SELECTOR, "body > div > div.workseditor-content").send_keys("파이썬으로 자동화한 메일 입니다.")
time.sleep(2)

# iframe 밖으로 나오기
driver.switch_to.default_content()

# 보내기 버튼
driver.find_element(By.CSS_SELECTOR, "#content > div.mail_toolbar.type_write > div:nth-child(1) > div > button.button_write_task").click()
