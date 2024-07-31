def single_root_words(root_word, *other_words):
# Функция принимает один параметр root_word и произвольное число параметров в виде кортежа other_words
# Создаю пустой список для вставки результатов выполнения функции
    same_words = list()
# Прохожу циклом по элементам (словам) кртежа other_words
    for x in other_words:
# Условный оператор принимает 2 условия в конструкции ИЛИ (OR)
# 1. слово из списка other_words содержит слово root_word
# 2. слово root_word содержит слово из списка other_words
# для нейтрализации зависимости от регистра символов оба слова используются в верхнем регистре
        if root_word.upper().find(x.upper()) != -1 or x.upper().find(root_word.upper()) != -1:
# В случае выполнения одного из условий добавляю элемент кортежа в результирующий список
            same_words.append(x)
# Наполненный список функция возвращает
    return same_words

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)