from selenium import webdriver
import time
driver = webdriver.Chrome("C:/chromedriver/chromedriver_win32/chromedriver")
i = 0
while i < 2:
    path = "C:/Users/81702/OneDrive/デスクトップ/NAIST_Ubi/sample_html/sample"+str(i)+".html"
    driver.get(path)
    time.sleep(3)
    i+=1
driver.close()