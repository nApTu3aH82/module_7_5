# -*- coding: utf-8 -*-
import os
import time

directory = os.getcwd()
for root, dirs, files in os.walk(directory):
    for file in files:
        filepath = os.path.join(file)
        file_size = os.path.getsize(file)
        filetime = os.path.getmtime(file)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        parent_dir = os.path.dirname(file)
        print(f'Обнаружен файл: {file}, Путь: {filepath}, '
              f'Размер: {file_size} байт, '
              f'Время изменения {formatted_time},'
              f'Родительская директория: {parent_dir}')
