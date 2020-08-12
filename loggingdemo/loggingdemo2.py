
# 用 logging.basicConfig()函数调整日志级别、输出格式等
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d  %H:%M:%S %a'    # 注意月份和天数不要搞乱了，这里的格式化符与time模块相同
                    )
logging.debug("msg1")
logging.info("msg2")
logging.warning("msg3")
logging.error("msg4")
logging.critical("msg5")