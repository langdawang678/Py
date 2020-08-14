from logging_demo.logger_handler import logger
import logging_demo.test2
from config.config import LoggerConfig
# 模拟不同的py文件调用同一个logger对象，方便把log信息输出到同一个log文件中
def main():
    logger.info("hi")

def hello():
    logger.error("hi")

# 从配置文件里获取值
value = LoggerConfig.logger_file
print(value)
