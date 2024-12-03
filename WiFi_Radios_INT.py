from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import datetime

# 打开Chrome
driver = webdriver.Chrome()
#driver.get("https://tau-int.noc.plume.com/login")
driver.get("https://tau-dev3.noc.plume.com/login")
driver.implicitly_wait(30)
driver.maximize_window()

# 登录dev3
driver.find_element(By.XPATH, r"/html/body/app/ng-component/div[1]/div[2]/div/div/tabs/div/div[2]").click()
driver.find_element(By.XPATH,r"/html/body/app/ng-component/div[1]/div[2]/div/div/tabs/tab[2]/div/div/div/input[1]").send_keys("c-xin.guo@charter.com")
driver.find_element(By.XPATH,r"/html/body/app/ng-component/div[1]/div[2]/div/div/tabs/tab[2]/div/div/div/input[2]").send_keys("Xin@Plume")
driver.find_element(By.XPATH,r"/html/body/app/ng-component/div[1]/div[2]/div/div/tabs/tab[2]/div/div/div/button").click()
driver.implicitly_wait(30)
print("DEV3 登录成功")
# 查找node
   #允许cookie和dev3版本release
driver.find_element(By.XPATH, r"/html/body/modal/div[2]/div[3]/button").click()
driver.find_element(By.XPATH, r"/html/body/app/cookie/div/div[2]").click()
driver.find_element(By.XPATH,r"/html/body/app/ng-component/header/div[1]/div/div[2]/div/div[1]/slidetoggler/div[1]/div[3]").click()
# node ID
driver.find_element(By.ID, r"search-input").send_keys("671a1c0f4a4c30000bba4456")
sleep(5)
driver.find_element(By.XPATH, r"/html/body/app/ng-component/header/div/div/div[2]/div/div[3]/div/div").click()
sleep(10)
print("ID 查找成功")
# 進入Configuration
# 滚動到特定元素Configuration
element = driver.find_element(By.XPATH, r"/html/body/app/ng-component/side-menu/div[1]/div[4]")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
sleep(5)
# 列印訊息
print("滚動到特定元素Configuration")
driver.find_element(By.XPATH, r"/html/body/app/ng-component/side-menu/div[1]/div[4]").click()
driver.implicitly_wait(30)
driver.find_element(By.XPATH,r"//*[@id='conf-wifiradio']/div/collapsiblebox/div/div/icon").click()
driver.implicitly_wait(10)
print("进入WiFi Radios页面")
checkbox = driver.find_element(By.XPATH,r"//*[@id='conf-wifiradio']/div/collapsiblebox/div/div[2]/div/div/div/div[1]/div[2]/div/label")
#判定
close = "checked"
ifcheckbox = close in checkbox.get_attribute("class")
if (ifcheckbox):
    print("----------WiFi Radios未被关闭，开始测试---------")
else:
    driver.find_element(By.XPATH,r"//*[@id='conf-wifiradio']/div/collapsiblebox/div/div[2]/div/div/div/div[1]/div[2]/div/label").click()
    print("-------WiFi Radios被关闭，已打开，开始测试-------")
sleep(10)

i=0
while i<100:  #测试次数
    i+=1
    #off
    driver.find_element(By.XPATH,r"//*[@id='conf-wifiradio']/div/collapsiblebox/div/div[2]/div/div/div/div[1]/div[2]/div/label").click()
    print("第", i, "次关WiFi Radios")
    sleep(300)

    #on
    driver.find_element(By.XPATH,r"//*[@id='conf-wifiradio']/div/collapsiblebox/div/div[2]/div/div/div/div[1]/div[2]/div/label").click()
    print("第", i, "次开WiFi Radios")
    sleep(300)

print("--------------开关",i,"次测试完成--------------")

driver.close()