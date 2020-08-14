from loggingdemo.logger_handler import logger

# 模拟不同的py文件调用同一个logger对象，方便把log信息输出到同一个log文件中
def main():
    logger.info("hi")

def hello():
    logger.error("hi")

