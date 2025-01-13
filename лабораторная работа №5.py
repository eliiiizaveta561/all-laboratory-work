class Book:
    title = 'Преступление и наказание' #атрибут класса
    author = 'Достоевский'
    year = '1926'

    def get_info(self):
        return f'Название книги: {self.title}, Автор: {self.author}, Год издания:  {self.year}'

book = Book()


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_radius(self):
        return self.radius

    def set_radius(self, new_radius):
        self.radius = new_radius

y = Circle(7) #экземпляр
print(y.get_radius())
y.set_radius(17)
print(y.get_radius())