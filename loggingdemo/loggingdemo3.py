"""
logging日志模块相关类及其常用方法介绍
与logging四大组件相关的类：Logger, Handler, Filter, Formatter。
组件名称	对应类名	功能描述
日志器	Logger	提供了应用程序可一直使用的接口
处理器	Handler	将logger创建的日志记录发送到合适的目的输出
过滤器	Filter	提供了更细粒度的控制工具来决定输出哪条日志记录，丢弃哪条日志记录
格式器	Formatter	决定日志记录的最终输出格式
"""


'''
1.日志收集器logger（日记本）
2.日志收集器级别 level
3.日志处理器handler（不同记号的笔）
4.日志处理器级别设置
5.logger.addHandler(handler)
6.设置日志格式format，日期；重要程度；分类（工作，生活）；内容fmt=logging.Format()
7.添加日志处理器,handler.setFormat

'''
import logging
logger = logging.getLogger("python")  # 设置logger名字，默认为root

# 设置级别（全大写）
# logger.setLevel("DEBUG")
logger.setLevel("DEBUG")

# FileHandler
handler = logging.FileHandler("FileHandler.txt")
handler.setLevel('DEBUG')

# StreamHandler
# handler类的默认级别是warning，默认是控制台输出,即StreamHandler
console_handler = logging.StreamHandler()  # 这里不能少括号,否则不是对象了，下面的就会提示少参数
console_handler.setLevel("DEBUG")


# handler设置级别：handler.setLevel('WARNING')
'''
handler设置的等级比logger的高,注意比较两者同时设定不同的级别时，最终的输出
'''

# 添加handler
logger.addHandler(handler)
logger.addHandler(console_handler)

# handler设置格式
fmt = logging.Formatter('%(asctime)s %(filename)s %(levelname)s %(message)s')
handler.setFormatter(fmt)   # 此时handler中写入的txt文件有log，控制台有其他级别的log。满足不同的需求

logger.debug("debug")
logger.info("info")
logger.warning("warning")


