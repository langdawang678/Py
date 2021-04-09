def loopProcess():
    while 1:
        a = input("\n输入0 退出程序，关闭浏览器\n"
                  "输入1 继续等待输入，不退出程序\n"
                  "输入2 继续上传执行\n"
                  "输入333 删除【成功】和【太迟了】的文件\n"
                  "输入4 获取邮件附件\n"
                  "请输入....:")
        if a == "":
            print("\n------请勿直接键入回车键，请重新输入...")
            continue  # 兼容直接回车
        try:
            int(a)
        except ValueError:
            print("------输入数字错误，请重新输入...")
            continue
        if int(a) == 0:
            print("\n------程序退出------\n")
            # pageMK.quitBrowser()
            break
        elif int(a) == 1:
            print("\n------继续等待输入------\n")
            continue
        elif int(a) == 2:
            print("\n------开始执行上传程序-------")
            # handleFile()
        elif int(a) == 333:
            print("\n------删除【成功】和【太迟了】的文件-------\n")
            # clearFile()
        elif int(a) == 4:
            print("\n------开始执行邮件附件下载程序-------\n")
            lastNum = input("请输入最近的邮件数(输入非数字，返回到主菜单)....:")
            try:
                int(lastNum)
                # doEmail(lastNum=str(lastNum))
            except ValueError:
                print("!!!输入错误，请输入数字...")
            finally:
                pass
        else:
            print("\n!!!输入错误，请重新输入...\n")
            continue


if __name__ == '__main__':
    loopProcess()
