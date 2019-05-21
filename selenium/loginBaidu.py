#login baidu
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://passport.baidu.com/v2/?login&tpl=mn&u=http%3A%2F%2Fwww.baidu.com%2F&sms=5")

driver.find_element_by_id("TANGRAM__PSP_3__footerULoginBtn").click()
driver.find_element_by_id("TANGRAM__PSP_3__userName").send_keys("langdawang678@sina.com")
driver.find_element_by_id("TANGRAM__PSP_3__password").send_keys("238088$$")

driver.find_element_by_id("TANGRAM__PSP_3__submit").click()

print (driver.find_element_by_id("TANGRAM__PSP_3__submit").size)
'''
或者:
size=driver.find_element_by_id("TANGRAM__PSP_3__submit").size
print (size)
其他：text、get_attribute(name/id/type)、is_displayed()

