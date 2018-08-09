import os

FILES_DIR = 'Migrations/'


def print_files(files):
    for file in files:
        print(file)


def main_search(success_files):
    while True:
        word = input('Введите слово,по которому будем совершать поиск файлов (чтобы выйти ничего не вводите): ')
        if not word:
            main_out(success_files)
            break

        files_copy = success_files.copy()
        print('-----ИЩЕМ ФАЙЛЫ-----')
        for file in files_copy:
            with open(file, encoding='utf8') as sql_file:
                if word not in sql_file.read():
                    success_files.discard(sql_file.name)

        print('\n'.join(list(success_files)))
        print('-----ЗАКОНЧИЛИ ИСКАТЬ-----')


def entry():
    suitable_files = set()
    for filename in os.listdir('Migrations'):
        file = os.path.join(FILES_DIR, filename)
        if file.endswith('.sql'):
            suitable_files.add(file)
    print('Мы нашли все sql-файлы в папке Migrations')
    main_search(suitable_files)


def main_out(success_files):
    print('Найденные файлы: ')
    print_files(success_files)
    print('Всего: {}'.format(len(success_files)))


if __name__ == '__main__':
    entry()
