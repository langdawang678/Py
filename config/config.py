"""
python配置文件的格式
1、Python文件作为模块，py文件作为配置的文件
2、yaml文件， .yml  .yaml  pyyaml库
    语法：http://www.ruanyifeng.com/blog/2016/07/yaml.html
    读取：
3、 .ini文件， .conf文件，比较老，但有公司在用。数据类型是字符串（跳过）
"""

# 根据需要，灵活配置在类或者 变量中
import sys


class LoggerConfig:
    logger_name = "python"
    logger_file = "python.txt"
    level = "DEBUG"


class ProductLoggerConfig(LoggerConfig):
    level = "WARING"


# 例如根据平台判断需要用到的log的类型
if sys.platform == "linux":
    config = ProductLoggerConfig
else:
    config = LoggerConfig

