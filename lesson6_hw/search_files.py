import os

FILES_DIR = 'Migrations/'
cur_success_files = set()


def print_files(files):
    for file in files:
        print(file)


def main_search():
    while True:
        word = input('Введите слово,по которому будем совершать поиск (чтобы выйти ничего не вводите): ')
        if word == '':
            break

        files_copy = cur_success_files.copy()
        print('-----ИЩЕМ ФАЙЛЫ-----')
        for file in files_copy:
            with open(file, encoding='utf8') as sql_file:
                if word not in sql_file.read():
                    cur_success_files.discard(sql_file.name)

        print_files(cur_success_files)
        print('-----ЗАКОНЧИЛИ ИСКАТЬ-----')


first_word = input('Введите слово,по которому будем совершать поиск (чтобы выйти ничего не вводите): ')
if first_word != '':
    for filename in os.listdir('Migrations'):
        file = FILES_DIR + filename
        if file.endswith('.sql'):
            with open(file, encoding='utf8') as sql_file:
                if first_word in sql_file.read():
                    cur_success_files.add(sql_file.name)

    print_files(cur_success_files)
    main_search()
    print('Найденные файлы: ')
    print_files(cur_success_files)

print('Всего: {}'.format(len(cur_success_files)))
