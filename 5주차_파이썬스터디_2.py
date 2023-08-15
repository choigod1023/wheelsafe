# 라이브러리 불러옴
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pyautogui
import time

# 실행경로와 드라이버 객체 생성

driver = webdriver.Chrome()
driver.get("https://cafe.naver.com/joonggonara/1005170350")
time.sleep(3)
driver.switch_to.frame('cafe_main')

tex = driver.find_element(
    By.XPATH, '//*[@id="app"]/div/div/div[2]/div[1]/div[1]/div/h3').text
print(tex)
