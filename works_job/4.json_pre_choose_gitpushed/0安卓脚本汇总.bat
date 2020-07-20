@echo off

:start
echo 输入对应数字选择功能:
echo     [0]    adb devices查看
echo     [1]    x1/X1/M1相关命令
echo     [2]    cc/cclite相关命令
echo     [9]    adb reboot
echo     [99]   exitcmd
set /p num=请输入:
echo.
if "%num%"=="0" (GOTO adbdevices) 
if "%num%"=="1" (GOTO X1C1M1) 
if "%num%"=="2" (GOTO CC)
if "%num%"=="9" (GOTO reboot)
if "%num%"=="99"(GOTO exitcmd)
echo.

:exitcmd
exit

:adbdevices
adb devices
GOTO start

:reboot
adb reboot
GOTO start


:X1C1M1
echo 输入对应数字选择C1X1M1功能:
echo     [0]    rm设备端log
echo     [1]    pull /data/syslog.log
echo     [2]    cat 配置的/data/smartbox/prodconf.json
echo     [3]    pull /usr/lib/smartbox导出默认的配置文件
echo     [4]    push 修改后的prodconf.json到/data/smartbox并重启
echo     [9]    返回顶层
set /p num=请输入:
echo.
if "%num%"=="0" GOTO  rmlogs
if "%num%"=="1" GOTO  pulllogs
if "%num%"=="2" GOTO  catprod
if "%num%"=="3" GOTO  pulldefault
if "%num%"=="4" GOTO  pushconfig
if "%num%"=="9" GOTO  start
:rmlogs
adb shell rm /data/syslog.log*
GOTO X1C1M1
:pulllogs
adb pull /data/syslog.log
GOTO X1C1M1
:catprod
echo 若提示“ No such file or directory”,则为线上
adb shell cat /data/smartbox/prodconf.json
GOTO X1C1M1
:pulldefault
adb pull /usr/lib/smartbox/prodconf.json
GOTO X1C1M1
:pushconfig
adb push prodconf.json /data/smartbox
adb shell sync
adb reboot
echo 导入成功，设备重启中
echo    
GOTO X1C1M1





:CC
echo 输入对应数字选择CC功能:
echo     [0]    setprop CC/CClite环境
echo     [1]    截图cc到当前目录
echo     [2]    启动iotMainActivity
echo     [3]    dumpsys genie.iot
echo     [4]    dumpsys iotx.linkvisual
echo     [5]    smartapp
echo     [8]    monkey10mins
echo     [9]    返回顶层

set /p num=请输入:
echo.
if "%num%"=="0" GOTO  prechoose
if "%num%"=="1" GOTO  screencap
if "%num%"=="2" GOTO  iotMainActivity
if "%num%"=="3" GOTO  com.alibaba.ailabs.genie.iot
if "%num%"=="4" GOTO  com.aliyun.iotx.linkvisual
if "%num%"=="5" GOTO  com.alibaba.ailabs.genie.smartapp
if "%num%"=="8" GOTO  monkey
if "%num%"=="9" GOTO  start

:prechoose
set /p num=请输入数字并按回车确认：0等于online; pre1; pre2; pre8:
if /i "%num%"=="0" goto :0
if /i "%num%"=="1" goto :1
if /i "%num%"=="2" goto :2
if /i "%num%"=="8" goto :8
:0
adb shell setprop persist.sys.genie.env 0
adb reboot
@echo pre0 rebooting
GOTO CC
:1
adb shell setprop persist.sys.genie.env 1
adb reboot
@echo pre1 rebooting
GOTO CC
:2
adb shell setprop persist.sys.genie.env 2
adb reboot
@echo pre2 rebooting
GOTO CC
:8
adb shell setprop persist.sys.genie.env 8
adb reboot
@echo pre8 rebooting
GOTO CC

:screencap
adb shell screencap -p /sdcard/01.png
adb pull /sdcard/01.png
GOTO CC

:iotMainActivity
adb shell am start -n com.alibaba.ailabs.genie.iot/com.alibaba.ailabs.genie.iot.MainActivity
GOTO CC

:com.alibaba.ailabs.genie.iot
@echo adb shell dumpsys package com.alibaba.ailabs.genie.iot
adb shell dumpsys package com.alibaba.ailabs.genie.iot | findstr "version"
GOTO CC

:com.aliyun.iotx.linkvisual
@echo adb shell dumpsys package com.aliyun.iotx.linkvisual
adb shell dumpsys package com.aliyun.iotx.linkvisual | findstr "version"
GOTO CC

:com.alibaba.ailabs.genie.smartapp
@echo adb shell dumpsys package com.alibaba.ailabs.genie.smartapp
adb shell dumpsys package com.alibaba.ailabs.genie.smartapp | findstr "version"
GOTO CC

:monkey
adb shell monkey -p com.alibaba.ailabs.genie.iot --throttle 500 -s 1000 --ignore-crashes --ignore-timeouts --ignore-security-exceptions --ignore-native-crashes --monitor-native-crashes -v -v -v 5000 >C:\Users\wb-chenxuanhuai\Desktop\monkey_log.txt
monkey
GOTO CC



3.远程诊断输入命令：setprop persist.adb.root 1
4.远程诊断输入命令：reboot
5.setprop persist.sys.genie.env 2
6.reboot

rem screencap
rem adb shell screencap -p /sdcard/01.png
rem cd C:\Users\wb-chenxuanhuai\Desktop
rem adb pull /sdcard/01.png
rem 
rem pre choose
rem adb shell setprop persist.sys.genie.env 1
rem adb reboot
rem 
rem autoinstall
rem @ECHO off  
rem @REM 无限循环的标签  
rem :LOOP  
rem ECHO 请插入手机…  
rem adb wait-for-device  
rem @REM 循环安装本目录下的APK文件  
rem FOR %%i IN (*.apk) DO (   
rem     ECHO 正在安装：%%i  
rem     adb install -r -d "%%i"  
rem     )  
rem ECHO 安装完毕；请更换下一台手机！
rem PAUSE  
rem GOTO LOOP  
rem @ECHO on
rem 
rem iot.MainActivity
rem adb shell am start -n com.alibaba.ailabs.genie.iot/com.alibaba.ailabs.genie.iot.MainActivity
rem 
rem 
rem 
rem adb reboot


