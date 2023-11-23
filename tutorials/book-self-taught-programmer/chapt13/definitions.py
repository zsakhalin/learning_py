# инкапсуляция
# Концепция 1:переменные(состояние) и методы группируются в единое целое - объект
# example245
class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def area(self):
        return self.width * self.length

    # Концепция 2: сокрытие внутренних данных класса дл предотвращения получения прямого доступа вне класса
    # example 247
class Data:
    def __init__(self):
        self.nums = [1, 2, 3, 4, 5]

    def changeData(self, index, n):
        self.nums[index] = n


data1 = Data()

data1.nums[1] = 100  # прямой доступ к полю класса
data1.changeData(2, 200)  # прямой доступ к методу класса и через него к полю
    # не похоже на инкапсуляцию, поэтому используется конвенция именования:(вместо существования закрытых методов/полей)
    # перед именем поля/метода, который предлагается считать инкапсулированным, ставится _
    # example 247
class LoginData:
    def __init__(self, login, password):
        self._login = login                 #хотя технически можно обратиться к _login, но формат имени говорит, что нельзя
        self.password = password            #поле с открытым доступом

    def changeLogin(self):                  #метод с открытым доступом, но сообщает, что _login менять нельзя
        print("u can't change login")

    def changePassword(self, newPassword):  #а вот password можно
        self.password = newPassword
        print("Password is changed")

    def _privateMethod(self):               #именование не предполагает, что этот метод можно вызывать изнутри
        pass


# абстракция
    # класс - способ смоделировать нечто, например, для представления человека можно создать класс Person.
    # смысл абстракции в том, что поля и методы класса зависят от решаемой задачи: для банка важны паспортные данные,
    # но не важны физ параметры

# полиморфизм
    # почитать об этом в другом каком-нибудь источнике, потому как смысл понятен, а реализация ниразу...

# наследование
    # возможность использовать поля/методы уже существующего класса(родителя), не создавая их заново в наследнике

class Shape:                            #класс родитель
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def printSize(self):
        print(f"width = {self.width}, length = {self.length}")
    def showInfo(self):
        print(f"this is shape")

class Rectangle(Shape):                 # класс наследник
    def findArea(self):                 # конструктор уже есть в родительском классе Shape, а это уже новый метод
        print(f"area = {self.width * self.length}")
    def showInfo(self):                # переопределение унаследованного метода
        print(f"[{self.width}, {self.length}]")

rect1 = Rectangle(1, 1)
rect1.printSize()                       # хотя printSize не определён для Rectangle, но его можно использовать
                                        # из-за наследования от Shape
rect1.findArea()                        # метод определён уже в самом Rectangle, а не унаследован от Shape
rect1.showInfo()                        # вызов метода, который унаследован, но работает иначе из-за переопределения

# композиция


class Person:
    def __init__(self, name):
        self.name = name
    def introduceSelf(self, petName):
        print(f"Hi, I'm {self.name}\n My pet is {petName}")


class Pet:
    def __init__(self, name, holder):
        self.name = name
        self.holder = holder


pers1 = Person("personName")            # Экземпляр одного класса можно
dog1 = Pet("petName", pers1)            # передать как параметр экземпляру другого класса
print(dog1.holder.name)                 # и через объект другого класса обращаться к полям
dog1.holder.introduceSelf(dog1.name)    # и методам переданного объекта