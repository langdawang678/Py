"""
本质:s1 + s2 = s1.__add__(s2)
"""

class MyStr(object):
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return self.data

    def __add__(self, other):
        return self.data + other.data

    def __sub__(self, other):
        return self.data.replace(other.data, "")


s1 = MyStr("ssss111")
s2 = MyStr("ssss2222")
print(s1)
print(s2)

s3 = MyStr(s1 + s2)  # s1 + s2 = s1.__add__(s2)
print(s3)
print(s3 - s1)
