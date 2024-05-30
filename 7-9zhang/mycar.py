import car
my_new_car=car.Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer() 

import chapter9
Admin=chapter9.Admin(1)
Admin.privileges.show_privilege()