import os
from time import sleep

str1 = os.system('adb devices')
# 半小时为例，不容易被休眠断网之类的
sleep(1800)

# 解锁
os.system('adb shell input keyevent 26')
os.system('adb shell input swipe 500 1000 100 100')

# 打开dd
os.system('adb shell am start com.alibaba.android.rimet/com.alibaba.android.rimet.biz.LaunchHomeActivity')
#同 adb shell input tap 150 190

# 登录动作需要上一次adb shell pm clear com.xxx

##保证无弹窗影响

# 底部中间
sleep(6)
os.system('adb shell input tap 550 1850')

# 下拉出现kaoqing
sleep(6)
os.system('adb shell input swipe 500 1000 400 800')

# 点击kaoqing
sleep(6)
os.system('adb shell input tap 918 1614')

# # 点击daka，调试慎点
# # sleep(6)
# # #####os.system('adb shell input tap 500 1150')

# 截图到桌面，查看结果
sleep(6)
os.system('adb shell screencap -p /sdcard/01.png')
os.system('adb pull /sdcard/01.png')

# 判断是否为成功的图像，如果为false，则rerun
# todo

# 关闭
os.system('adb shell am force-stop com.alibaba.android.rimet')
