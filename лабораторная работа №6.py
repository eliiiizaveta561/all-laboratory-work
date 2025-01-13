#zadanie 1
class UserAccount:
    def __init__(self, username, email, __password):
        self.username = username
        self.email = email
        self.__password = hash(__password)

    def set_password(self, __new_password):
        self.__password = __new_password
        self.__password = hash(self.__password)

    def check_password(self, password):
        return hash(password) == self.__password


user1 = UserAccount('Liza', 'elizaveta.ru', '1234')
print(user1.check_password('12344'))
user1.set_password('12334')
print(user1.check_password('1123'))


# #zadanie 2
# class Vehicle:
#     def __init__(self, make, model):
#         self.make = make
#         self.model = model
#
#     def get_info(self):
#         print( f'Марка: {self.make}, Модель: {self.model}')
#
# class Car(Vehicle):
#     def __init__(self, make, model, fuel_type):
#         self.fuel_type = fuel_type
#         super().__init__(make, model)
#
#     def get_info(self):
#         print(f'Марка: {self.make}, Модель: {self.model}, Тип топлива: {self.fuel_type}')
#
# car1 = Vehicle('BMW', 'M5')
# car1.get_info()
# car1 = Car('BMW', 'M5', 'AI-95')
# car1.get_info()
