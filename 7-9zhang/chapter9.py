# class Dog:
#     def __init__(self, name, age) -> None:
#         self.name=name
#         self.age=age
    

#     def sit(self):
#         print(f"{self.name} is now sitting.")
    

#     def roll_over(self):
#         print(f"{self.name} rolled over!")


# my_dog = Dog('while', 6)

# print(f"My dog's name is {my_dog.name}.")
# print(f"My dog is {my_dog.age} years old.")
# my_dog.sit()
# my_dog.roll_over()


# class Restaurant():
#     def __init__(self, restaurant_name, cuisine_type) -> None:
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
#         self.number_serves = 0


#     def describe_restaurant(self):
#         print(f"{self.restaurant_name} {self.cuisine_type}")


#     def open_restaurant(self):
#         print(f"{self.restaurant_name} is open")
    
    
#     def set_number_served(self, peonum):
#         self.number_serves=peonum
#         return self.number_serves
    

#     def increment_number_served(self,peopletoday):
#         self.number_serves= int(peopletoday) * 2
#         return self.number_serves
    
# restaurant = Restaurant("amaya", "chinafood")
# restaurant.set_number_served(44)
# restaurant.increment_number_served(23)
# print(restaurant.number_serves)

# my_Restaurent = Restaurant("amaya", "chinafood")
# print(my_Restaurent.restaurant_name)
# print(my_Restaurent.cuisine_type)
# my_Restaurent.describe_restaurant()
# my_Restaurent.open_restaurant()

# my_Restaurent1 = Restaurant("111", "222")
# my_Restaurent1.describe_restaurant()

# my_Restaurent2 = Restaurant("333", "444")
# my_Restaurent2.describe_restaurant()


# class Car:
#     def __init__(self, make, model, year) -> None:
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0
    

#     def get_descriptive_name(self):
#         long_name=f"{self.year} {self.make} {self.model}"
#         return long_name
    

#     def read_odometer(self):
#         print(f"This car has {self.odometer_reading} miles on it.")


#     def update_odometer(self,mile):
#         self.odometer_reading=mile

# my_new_car = Car('audi', 'a4', 2024)
# print(my_new_car.get_descriptive_name())

# # my_new_car.odometer_reading=23
# my_new_car.update_odometer(5)
# my_new_car.read_odometer()


class user:
    
    def __init__(self, login_attempts) -> None:
        self.login_attempts=login_attempts
        
        
        

    def increment_login_attempts(self):
        int(self.login_attempts)
        self.login_attempts+=1
        return self.login_attempts


    def reset_login_attempts(self):
        self.login_attempts=0
        return int(self.login_attempts)

    
# instance_user=user(56)
# print(instance_user.login_attempts)
# print(instance_user.increment_login_attempts())
# print(instance_user.reset_login_attempts())


# class new_user(user):
#     def __init__(self, login_attempts) -> None:
#         super().__init__(login_attempts)

# newuser=new_user(1)
# print(newuser.login_attempts) 


# class IceCreamStand(Restaurant):
#     def __init__(self, restaurant_name, cuisine_type) -> None:
#         super().__init__(restaurant_name, cuisine_type)
#         self.flavors=["suan", "tian", "ku", "la"]

    
#     def show_flavors(self):
#         for i in self.flavors:
#             print(i)

    
# IceCreamStand=IceCreamStand("Ice", "Cream")
# IceCreamStand.show_flavors()


class Admin(user):
    def __init__(self, login_attempts, ) -> None:
        super().__init__(login_attempts)
        self.privileges=Privileges()
        
        


class Privileges:
    def __init__(self) -> None:
        self.privileges=["can add post", "can delete post", "can ban user"]
    

    def show_privilege(self):
        print(self.privileges) 

# Admin=Admin(1)
# Admin.privileges.show_privilege()


