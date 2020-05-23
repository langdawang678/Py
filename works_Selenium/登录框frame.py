from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome()
driver.get('开放平台')
driver.maximize_window()

driver.switch_to.frame("阿狸爸爸-login-box")
driver.find_element_by_xpath('//*[@id="fm-login-id"]').send_keys("XXXX")
driver.find_element_by_xpath('//*[@id="fm-login-password"]').send_keys("XXXX")
huakuai = driver.find_element_by_xpath('//*[@id="nc_1_n1z"]')
# ActionChains(driver).drag_and_drop(element, target).perform()

driver.find_element_by_xpath('//*[@id="login-form"]/div[4]/button').click()
print(driver.title)
