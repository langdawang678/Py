import time
import os

lead_time = 1
trigger_time = 1583416800-lead_time

# 从分享进入商品页面
action1 = "adb shell input tap 528 1518"
# action1 = "adb shell input tap 819 1875"

# 提交订单；选择规格后的确定；立即购买；
action2 = "adb shell input tap 888 2258"

os.system("adb devices")
# 保持睡眠，直到还剩下5秒
sleep_time = int(trigger_time - time.time() - 5)
time.sleep(sleep_time)

print('约提前5秒开始执行：',time.time())
for i in range(0, 1000000000):
    now = time.time()
    # print(i, "当前时间戳为:", now)
    if now >= trigger_time:
        print("触发时间：", now)
        os.system(action1)  # 进入商品
        # time.sleep(0.05)    # 这里等待时间不够，就会导致下一条失败，就多了0.4秒，所以尽量算好时间一次成功
        os.system(action2)  # 立即购买
        # time.sleep(0.15)
        os.system(action2)  # 提交订单
        os.system(action2)
        os.system(action2)
        print("action1消耗时间：", time.time()-now)
        break
# 每条命令的平均延迟是 0.38秒到0.4秒之间