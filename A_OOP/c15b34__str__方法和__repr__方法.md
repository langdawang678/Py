

## 问题：交互环境代码演示中 print(a)和a，返回的不一样
![](.c15b34__str__方法和__repr__方法_images/c15b34__str方法和__repr__方法.png)

## 原因：因为底层触发的魔术方法不一样
print方法触发的__srt__方法  
直接输出是触发的__repr__方法  


__srt__ 输出的内容可以理解为是给用户看的，用户不关心是说明数据类型，只关心内容  
__repr__ 可以理解为是给开发看的，开发看到这个一眼就能确认是字符转类型  

## 调用逻辑：
![](.c15b34__str__方法和__repr__方法_images/3818b5af.png)
可以理解为__repr__是__str__备胎  



## 注意点：
重写的Str和repr方法：类中有str就用Str，没有就用repr ，都没有就用object中的str方法。  


参考代码：
https://www.cnblogs.com/jiangmingbai/p/10909449.html#__srt__%E6%96%B9%E6%B3%95%E5%92%8C__repr__%E6%96%B9%E6%B3%95
```
class MyStrRepr(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def __str__(self):
        print("出发__str__方法")
        return self.name # 不返回 或者返回的类型不是字符串的时候会报错

    def __repr__(self):
        print("出发__repr__方法")
        return "MySrtRepr.object.name-%s" % self.gender


s = MyStrRepr("111", "男")
print(s)  # print 触发__str方法
str(s)  # srt 触发__srt__
format(s)  # format 触发__srt__
res = repr(s)  # repr 触发__repr__   程序员输出方式
print(res)
```