from oop.car import Car


class Battery():
    """一次模拟电动汽车电瓶的简单尝试"""

    def __init__(self, battery_size=70):
        # 这个形参是可选的： 如果没有给它提供值， 电瓶容量将被设置为70。
        """初始化电瓶的属性"""
        self.battery_size = battery_size

    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        """打印一条消息， 指出电瓶的续航里程"""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        message = "This car can go approximately " + str(range) + " miles on a full charge."
        print(message)


class ElectricCar(Car):
    # 定义子类时， 必须在括号内指定父类的名称。
    def __init__(self, make, model, year):
        """初始化父类的属性"""
        Car.__init__(self, make, model, year)
        '''
        上面的方法虽然可以实现基本的功能，但是可拓展性比较差。
        用super().__init__(make, model, year) ，P85
        1、是用来解决多重继承问题的，直接用类名调用父类方法在使用单继承的时候没问题.
        2、当父类名字发生修该时下面就必须进行修改，这时候可以使用super()方法就可以解决这问题。
        '''
        self.battery = Battery()
        '''*创建一个新的Battery 实例（由于没有指定尺寸， 因此为默认值70 ）
        并将该实例存储在属性self.battery 中。
        每个ElectricCar 实例都包含一个自动创建的Battery 实例。'''
