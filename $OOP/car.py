
class Car:
    """一次模拟汽车的简单尝试"""

    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        '''类中的每个属性都必须有初始值， 哪怕这个值是0或空字符串。'''
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """打印一条指出汽车里程的消息"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print('you cannot change smaller')

    def increment_odometer(self, miles):
        """将里程表读数增加指定的量"""
        self.odometer_reading += miles

class Battery:
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
            ranges = 240
        elif self.battery_size == 85:
            ranges = 270
        message = "This car can go approximately " + str(ranges) + " miles on a full charge."
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


# 打开模块car ， 并导入其中的Car 类。就像它是在这个文件中定义的一样
my_new_car = Car('audi', 'a4', 2016)
''''#要修改属性的值， 最简单的方式是通过实例直接访问它。
my_new_car.odometer_reading = 23
'''
my_new_car.get_descriptive_name()

my_new_car.update_odometer(26)
my_new_car.read_odometer()

my_used_car = Car('subaru', 'outback', 2013)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23500)
my_used_car.read_odometer()
my_used_car.increment_odometer(100)
my_used_car.read_odometer()


my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()