from oop.car import Car

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
