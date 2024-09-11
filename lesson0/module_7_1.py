from pprint import  pprint

class Product:
    def __init__(self, name: str, weight: float, category: str):
# При инициализации экземпляра класса Product
# определяю атрибуты: name, weight, category, задаю тип данных каждому атрибуту
        self.name = name
        self.weight = weight
        self.category = category
    def __str__(self):
# Специальный метод __str__ возвращает форматированную строку
        return '{name}, {weight}, {category}'.format(name = self.name, weight = self.weight, category = self.category)

class Shop:
    def __init__(self):
# При инициализации создаю инкапсулированный атрибут __file_name для объекта класса Shop
        self.__file_name = 'products.txt'

    def get_products(self):
# Для получения списка продуктов из файла использую конструкцию with
# файл открывается в режиме чтения
        with open(self.__file_name, 'r') as file:
            return(file.read())
# Такой способ не требует закрытия файла
# соответствнно код короче, а также не используется лишняя переменная result
#        file = open(self.__file_name, 'r')
#        result = (file.read())
#        file.close()
#        return result

    def add(self, *products):
# Перед добавлением строки в файл получаю список продуктов из файла существующим методом get_products
        list = Shop.get_products(self)
# Открываю файл в режиме добавления строк до цикла, иначе файл будет открываться несколько раз
        file = open(self.__file_name, 'a')
# В цикле обрабатываю переданные методу экземпляры продуктов
# методом find производится поиск имени каждого продукта в тексте, полученном ранее в переменную list
        for p in products:
            if list.find(p.name) == -1:
# Если такой продукт не найден в файле, производится запись строки с продуктом в файл
                file.write('{name}, {weight}, {category}\n'.format(name=p.name, weight=p.weight, category=p.category))
            else:
# Если такой продукт уже присутствует в файле, выводится соответствующее сообщение
                print('Продукт {name} уже есть в магазине'.format(name=p.name))
# После прохождения цикла поиска продукта файл обязательно закрываю
        file.close()

# Выполнение
s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())