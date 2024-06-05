class Employee:
    def __init__(self, name, age, money) -> None:
        self.name = name
        self.age = age
        self.money = int(money)
    
    def give_raise(self, add=5000):
        self.money += int(add)
        return self.money
