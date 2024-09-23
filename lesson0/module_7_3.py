#from pprint import pprint
class WordsFinder:
    def __init__(self, *files: list):
# Формирую корректный список файлов
# Обрабатываются различные варианты переданного параметра:
# 'file1.txt', 'file2.txt', 'file3.txt'
# 'file1.txt, file2.txt', 'file3.txt'
# 'file1.txt, file2.txt, file3.txt'

        file_names_str = str() # Создаю пустую строку для имён файлов
# Формирую строку из переданных параметров (имён файлов)
# После цикла первый символ строки будет ','
        for file_name in list(files):
            file_names_str += ',' + file_name # Присоединяю имя файла к строке с именами
# Избавляюсь от пробелов в сформированной строке и от первого символа (',')
        file_names_str = file_names_str.replace(' ', '')
        file_names_str = file_names_str.replace(',', '', 1)
# Формирую список из имён файлов
        self.file_names = file_names_str.split(',')

    def get_all_words(self):
#        print('START get_all_words')
        all_words = {} # Словарь: ключ - название файла, значение - список из слов этого файла
# Цикл перебирает имена файлов
        for file_name in self.file_names:
            file_lines = str() # Создаю пустую строку для записи всех строк файла
# Открываю каждый файл
            with open(file_name, encoding='utf-8') as file:
                file_lines_list = list() # Создаю пустой список для строк файла
# Циклом каждую строку файла присоединяю к суммирующей строке c предыдущими строками файла
                for line in file:
                    file_lines += ' ' + line.rstrip('\n').lower()
                file_lines = file_lines.replace(' ', '', 1)
# Избавляюсь от пунктуации, заменяя сиволы пробелами
                for replace_symbol in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                    file_lines = file_lines.replace(replace_symbol, ' ')
# Избавляюсь от множественных пробелов
                for i in range(10, 1, -1):
                    file_lines = file_lines.replace(' ' * i, ' ')
# Формирую список из слов внутри файла
                file_lines_list = file_lines.split()
# Заполняю словарь
            all_words[file_name] = file_lines_list
        return all_words

    def find(self, word):
        result_dict = dict() # Создаю пустой словарь для возврата результата
# Получаю словарь всех слов во всех файлах через метод get_all_words
        all_words = self.get_all_words()
# Перебираю словарь и методом index в значениях ищу переданное слово в нижнем регистре
        for key, value in all_words.items():
            result_dict[key] = value.index(word.lower()) + 1
        return result_dict
        result_list = list()

    def count(self, word):
        result_dict = dict()  # Создаю пустой словарь для возврата результата
# Получаю словарь всех слов во всех файлах через метод get_all_words
        all_words = self.get_all_words()
# Перебираю словарь и методом count в значениях ищу количество совпадений с переданным словом
        for key, value in all_words.items():
            result_dict[key] = value.count(word.lower())
        return result_dict

#finder2 = WordsFinder('file1.txt', 'file2.txt', 'file3.txt')
#finder2 = WordsFinder('file1.txt, file2.txt', 'file3.txt')
#finder2 = WordsFinder('file1.txt, file2.txt, file3.txt')

finder2 = WordsFinder('test_file.txt')

print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего