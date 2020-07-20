# coding=utf-8
import xlwt
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time
import xlrd
import xlwt
import os
import sys
from xlutils.copy import copy


'''
option = webdriver.ChromeOptions()
option.add_argument('--incognito')
#隐身模式
#driver = webdriver.Chrome(chrome_options=option)
'''

# 获取当前目录文件，检查是否存在冲突或者文件不存在
listdir = os.listdir(os.getcwd())
if "对比结果.xls" not in  listdir or "rerun_result.xls" in listdir:
    print('''当前目录的excel文件名 设置错误或者文件冲突:
    1.确保《对比结果.xls》文件存在
    2.请先remove or rename 上一次的《rerun_result.xls》
    3.rerun this script
''')
# 也可用os.path.exist(filepath or filename)判断文件或目录是否存在
    sys.exit(0)



# 打开excel对象
workbook = xlrd.open_workbook('./对比结果.xls')
# 打开sheet_1 ,即【2.rerun的语料(这次fail,上次pass)】（sheet_0是对比结果）
sheet1 = workbook.sheets()[1]
# 读sheet1取列0（list）的被测试语料
sheet1_col0_corpus = sheet1.col_values(0)
# 读sheet1取列1（list）的被测试语境
sheet1_col1_context = sheet1.col_values(1)

num_corpus = len(sheet1_col0_corpus)
print("获取到的语料个数（含excel中单元格为空的）：", num_corpus)


driver = webdriver.Chrome()
driver.maximize_window()

# get测试环境：这里预发2固定
url = "https://ailabs.alibaba-inc.com/pre2/app/ai-qa/dialogue"
driver.get(url)

print(driver.title+ "\n"+"请在40秒内登陆个人域账号...")
time.sleep(40) # 用于个人账号的输入，浏览器代理时，会有强制登录验证。


# 清空、输入语境
def input_centext(i):
    textarea = driver.find_element_by_css_selector(".ant-input:nth-child(1)") # 定位语境输入框
    time.sleep(1)
    textarea.clear()
    textarea.send_keys(sheet1_col1_context[i])

context_row = 0  # 用于第0条的语境输入
# 执行测试语料
for statement in sheet1_col0_corpus:
    input_centext(context_row)
    driver.find_element_by_css_selector(".ant-input:nth-child(4)").send_keys(statement) # 定位语料输入框
    clickButton = driver.find_element_by_css_selector(".ant-btn:nth-child(5)")  # 定位确定按键
    clickButton.click()
    time.sleep(5) # 确保设备不会因并发二失败
    context_row += 1  # 执行一次后，语境到第二条
    # 修改每条执行间隔，5=五秒


# 使用xlutils建立copy，因xlrd无法写入、xlwt只能在新建时写入
# 覆写sheet1 用于xlwt写入
copybook = copy(workbook)
sheet1 = copybook.get_sheet(1)

# 执行完毕后，统一抓取log
for row in range(0, num_corpus):
    if row == 0:
        xpath_input = "//div[@id='box']/div/div/span" # 定位第0行的回显：输入语料
        xpath_output = "//div[@id='box']/div/div[2]" # 定位第0行的回显：返回结果
        xpath_traceID = '//*[@id="box"]/div/div[3]/div[9]/a[4]' # 定位第0行的回显：traceID

    else:
        xpath_input = "//div[@id='box']/div[" + str(row + 1) + "]/div/span" # 定位第X行的回显：输入语料 
        xpath_output = "//div[@id='box']/div[" + str(row + 1) + "]/div[2]"  # 定位第X行的回显：返回结果
        xpath_traceID = '//*[@id="box"]/div[' + str(row + 1) + ']/div[3]/div[9]/a[4]' # 定位第X行的回显：traceID

    # 记录输入的语料：
    input_text = driver.find_element_by_xpath(xpath_input).text
    sheet1.write(row, 0, input_text)
    # print("输入语料", row, input_text)

    # 记录输入的语境：
    sheet1.write(row, 1, sheet1_col1_context[row])

    # 记录答复：
    response_text = driver.find_element_by_xpath(xpath_output).text
    sheet1.write(row, 2, response_text)
    # print("输出答复：", row, response_text)

    # 记录traceid的url
    traceid_url = driver.find_element_by_xpath(xpath_traceID).get_attribute("href")
    sheet1.write(row, 3, traceid_url)
    # print("traceID：", row, traceid_url)
    # print('\n')
    copybook.save('rerun_result.xls')

print("执行结束，不关闭浏览器。可在本地结果和web上分析")
