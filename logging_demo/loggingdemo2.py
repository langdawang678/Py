# 演示logging模块的大概使用
# 用 logging.basicConfig()函数调整日志级别、输出格式等
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d  %H:%M:%S %a'  # 注意月份和天数不要搞乱了，这里的格式化符与time模块相同
                    )


def old_function():
    try:
        1 / 0
        # 1/1
        logging.info("代码没有问题")
    except Exception as e:
        logging.error(e)
    logging.warning("这个方法在下一个版本中会被抛弃")
    return "hello"


if __name__ == '__main__':
    old_function()
