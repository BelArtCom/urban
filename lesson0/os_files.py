import os, time

directory = '.'

for root, dirs, files in os.walk(directory):
    for file in files:
        filepath = root
        filetime = os.path.getmtime(os.path.join(root, file))
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = os.path.getsize(os.path.join(root, file))
        parent_dir = os.path.basename(root)
        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')


