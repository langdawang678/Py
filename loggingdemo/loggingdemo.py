import logging
'''
这说明默认的日志级别设置为WARNING（日志级别等级CRITICAL > ERROR > WARNING > INFO > DEBUG）

'''
# NOSET 最低级别，等于没写
logging.debug("这是一个debug信息")
logging.info("info信息")
logging.warning("这是一个告警信息")
logging.error("出错了")
logging.critical("崩溃了")

