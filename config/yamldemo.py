import yaml

with open('python.yml',encoding='utf-8') as f:
    # 注意查看yaml文件中的编码格式，否则中文会乱码
    # def load(stream, Loader=None):
    data = yaml.load(f, Loader=yaml.FullLoader)
    print(type(data))  # <class 'dict'>

