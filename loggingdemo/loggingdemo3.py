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
1.日志收集器logger
2.日志收集器级别
3.日志处理器handler
4.日志处理器级别设置
5.设置日志格式format
6.添加日志处理器

'''
import logging
logger = logging.getLogger("python")  # 设置logger名字，默认为root

# 设置级别（全大写）
logger.setLevel("DEBUG")


# 默认是warning，默认是控制台输出,即StreamHandler
# handler = logging.StreamHandler()
handler = logging.FileHandler("FileHandler.txt")


logger.info("hello")
logger.warning("world")


