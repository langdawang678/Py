
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time

option = webdriver.ChromeOptions()
option.add_argument('--incognito')
#����ģʽ

driver = webdriver.Chrome(chrome_options=option)
driver.maximize_window()
driver.get("xxxxxx")


driver.switch_to.frame("xxxxxxxxx")


print(driver.title)


driver.find_element_by_id('fm-login-id').send_keys("xxxxxx")
driver.find_element_by_id("fm-login-password").send_keys("xxxxx")
driver.find_element_by_id("fm-login-submit").submit()

time.sleep(5)
driver.find_element_by_link_text("�´���˵").click()

time.sleep(5)
driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div/div[1]/div/div/div[1]/div/span[1]').click()
#���ʵ�һ�����Ŀ��

#�˴������ж�

