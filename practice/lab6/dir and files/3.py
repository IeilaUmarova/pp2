import os
path = input('Введите путь: \n')
if os.path.exists(path):
    directories = [name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name))]
    files = [name for name in os.listdir(path) if os.path.isfile(os.path.join(path, name))]
    print("Папки:", ', '.join(directories))
    print("Файлы:", ', '.join(files))
else:
    print("Путь не существует")