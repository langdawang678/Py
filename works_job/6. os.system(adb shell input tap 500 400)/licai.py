#coding:utf-8
import os
import time

str1 = os.system("adb devices")
print(str1)

#lead_time=提前x秒触发脚本，因为点击发送本身要0.4秒左右
lead_time = 0.3
trigger_time = 1587542400-lead_time

#21:1587456000
#22:1587542400
#23:1587628800
#24:1587715200
# 保持睡眠，直到还剩下5秒
sleep_time = int(trigger_time - time.time() - 5)
time.sleep(sleep_time)


print('约提前5秒开始执行：',time.time())
for i in range(0, 1000000000):
    now = time.time()
    # print(i, "当前时间戳为:", now)
    if now >= trigger_time:
        print("触发时间：", now)
        # 每条命令的平均延迟是 0.38秒到0.4秒之间
        #从列表进入
        os.system("adb shell input tap 500 400")
        time.sleep(0.3)

        #买入
        os.system("adb shell input tap 550 2200")
        time.sleep(0.3)
        
        #协议勾选-平安金
        #建信少多个提示，就是70 1550
        os.system("adb shell input tap 70 1410")

        #金额输入框
        os.system("adb shell input tap 280 680")
        #数字1
        os.system("adb shell input tap 152 1800")
        #数字0
        os.system("adb shell input tap 440 2240")
        os.system("adb shell input tap 440 2240")
        os.system("adb shell input tap 440 2240")
        os.system("adb shell input tap 440 2240")

        #确定
        os.system("adb shell input tap 566 1600")
        
        print("action1消耗时间：", time.time()-now)
        break

