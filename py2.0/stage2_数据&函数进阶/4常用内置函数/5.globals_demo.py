"""
描述：
  globals() 以字典类型返回当前位置的全部全局变量
语法：
  globals()
参数：
  无
返回值：
  返回全局变量的字典。
"""
a = 'runoob'
print(globals())  # globals 函数返回一个全局变量的字典，包括所有导入的变量。
'''
res = {'__name__': '__main__',
       '__doc__': '\n描述：\n  globals() 函数会以字典类型返回当前位置的全部全局变量。\n语法：\n  globals()\n参数：\n  无\n返回值：\n  返回全局变量的字典。\n',
       '__package__': None, 
       '__loader__': < _frozen_importlib_external.SourceFileLoader object at0x7fe3059746d0 >, 
        '__spec__': None, 
        '__annotations__': {}, 
        '__builtins__': < module 'builtins'(built - in) >, 
        '__file__': '/Users/chenxuanhuai/PycharmProjects/Py/py2.0/stage2_数据&函数进阶/4常用内置函数/5.globals_demo.py', 
        '__cached__': None, 
        'a': 'runoob'}
'''
