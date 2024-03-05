# ООП-обьект ориент прога

P = 1, '', 1.2, True, None, [], {}, (), 1
p = tuple
print(type(p))


def a():
    ...


a()


# класс
class Car:
    # переменная внутри класса - свойсво класса
    fars = 'True'

    #констуктор класса
    def __init__(self,model,year,color):
        self.name=model
        self.year=year
        self.color=color

    #   функция внутри класса - метод
    def Fars(self):
        print(self.fars)

    # магический метод - функция класса
    def __str__(self):
        return f'привет {self.fars}'

    def __len__(self): ...


# обьект\эклемпляр класса
car = Car()
car2 = Car()
car3 = Car()

car3.Fars()

print(car3)
print(car2)
print(car)
print(len(car2))