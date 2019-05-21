from selenium import webdriver
'''导入 selenium 的 webdriver 包，只有导入 webdriver 包我们才能使用 webdriver API 进行自动化脚本
的开发。'''

browser = webdriver.Chrome()
#browser只是变量名，也可以用别的，如diver
browser.get("http://www.baidu.com")
'''获得浏览器对象后，通过HTML的get()方法，可以向浏览器发送get网址的请求。
'''
browser.find_element_by_id("kw").send_keys("selenium")
'''关于页面元素的定位后面将会详细的介绍，这里通过 id=kw 定位到百度的输入框，并通过键盘方法
send_keys()向输入框里输入 selenium 。多自然语言呀！
'''
browser.find_element_by_id("su").click()
'''这一步通过 id=su 定位的搜索按钮，并向按钮发送单击事件（ click() ）'''
# browser.quit //退出并关闭窗口的每一个相关的驱动程序。


print(browser.current_window_handle)
