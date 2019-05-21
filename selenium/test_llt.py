
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time
import xlrd

'''
option = webdriver.ChromeOptions()
option.add_argument('--incognito')
#����ģʽ
#driver = webdriver.Chrome(chrome_options=option)
'''

driver = webdriver.Chrome()
driver.maximize_window()

#��excel
test_excel=xlrd.open_workbook(r'xx')

#��sheet_0����ȡcol 0��list���Ĳ��Ի���������+�ﾳ��
sheet_0=test_excel.sheets()[0]
col_0=sheet_0.col_values(0)

#��sheet_1����ȡcol 0��list���ı���������
sheet_1=test_excel.sheets()[1]
col_1=sheet_1.col_values(0)

#get���Ի���������
driver.get(col_0[0])
print(driver.title)

#��ա������ﾳ
textarea= WebDriverWait(driver,10).until(lambda driver: driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[3]/div/div[2]/div[2]/textarea'))
textarea.clear()
textarea.send_keys(col_0[1])

#ִ�в�������
for statement in col_1:
    driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[3]/div/div[1]/div[2]/input').send_keys(statement)
    clickbuttion= WebDriverWait(driver,10).until(lambda driver: driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[3]/div/div[1]/div[2]/button[1]'))
    clickbuttion.click()
    time.sleep(3)