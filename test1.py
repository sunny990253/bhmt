import time
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
import cv2
import numpy as np

driver = webdriver.Chrome()

#導向巴哈
driver.get("https://ani.gamer.com.tw/")
time.sleep(2)

#找關鍵字吉伊卡哇
searchInput = driver.find_element(By.ID, "anime-search-sky")
searchInput.send_keys("吉伊卡哇" + Keys.ENTER)

#找到吉伊卡哇後點進影集
button = driver.find_element(By.CLASS_NAME, "theme-list-main")
button.click()
time.sleep(2)

#找吉伊卡哇第90集並跳轉
morebtn = driver.find_element(By.CLASS_NAME, "ani-season-more-btn")
morebtn.click()
time.sleep(1)

tag = driver.find_element(By.LINK_TEXT, "90")
tag.click()
time.sleep(1)

#同意政策
agree_button = driver.find_element(By.ID, "adult") 
agree_button.click()

#影片
video = driver.find_element(By.TAG_NAME, 'video')
time.sleep(45)
print("【請手動跳過浮層網站獎勵廣告，暫時還沒想到解法】\n思路目前有以下幾種:\n1.關閉獎勵影片\n2.處理獎勵影片選擇器\n  處理關閉獎勵影片選擇器\n3.浮層問題\n")

#檢查影片播放狀態
while True:
    #影片的目前播放時間和總長度
    current_time = driver.execute_script("return arguments[0].currentTime", video)
    duration = driver.execute_script("return arguments[0].duration", video)

    print(f"Current Time: {current_time}, Duration: {duration}")
    
    if current_time >= duration:
        print("影片已播放完畢")
        break

    time.sleep(10)  

#input()

#關閉瀏覽器
driver.quit()