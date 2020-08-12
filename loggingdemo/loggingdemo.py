import logging
'''
这说明默认的日志级别设置为WARNING（日志级别等级CRITICAL > ERROR > WARNING > INFO > DEBUG）

'''
logging.debug("debug不输出")
logging.info("info不输出")
logging.warning("warning_msg")
logging.error("error_msg")
logging.critical("critical_msg")

