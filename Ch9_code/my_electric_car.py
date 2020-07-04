"""一组可用于表示调用汽车的类"""

from car import ElectricCar

my_tesla = ElectricCar('tesla', 'mode s', 2016)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()