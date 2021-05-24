import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


url = 'https://test-platform.tuya-inc.top:7799/#/task/taskCaseRun?masterId=10406&taskModule=KA&taskId=17692&setId=38488&setName=1.1.5%E6%B5%8B%E8%AF%95%E7%94%A8%E4%BE%8B&caseId=339202'

caseNumber = 366
# url = input("请输入测试用例的执行界面:")
# caseNumber = int(input("请输入测试用例的条数:"))

# 选择优先级
location_priority = '//*[@id="testCaseRun"]/div[1]/div[2]/div[4]/div[2]/input'
location_pass = '//button//span[text()="通过"]'

location_read = '//*[@id="testCaseRun"]/div[2]/div/div[3]/div[4]/div/div/button/span'
location_undo = '//*[@id="testCaseRun"]/div[2]/div/div[3]/div[4]/div/button[4]/span'
driver = webdriver.Chrome()
driver.get(url)
time.sleep(20)

driver.get(url)
time.sleep(5)
print(driver.title)
# 选择优先级为P2
# driver.find_element_by_xpath(location_priority).select_by_index(3)
for i in range(caseNumber):
    print("iii", i)
    # driver.find_element_by_xpath(location_pass).click()
    ele = WebDriverWait(driver,10,0.5).until(EC.presence_of_element_located((By.XPATH, location_pass)))
    ele.click()
    time.sleep(3)

    # WebDriverWait(driver, 10).until(lambda driver: driver.findElement(By.XPATH(location_pass)));
    # AttributeError: 'WebDriver' object has no attribute 'findElement'

    # driver.find_element_by_xpath(location_read).click()
