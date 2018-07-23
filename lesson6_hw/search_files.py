import os
from pprint import pprint
from glob import glob


abs_path = os.path.dirname(os.path.realpath(__file__))
abs_path = os.path.join(abs_path, 'Migrations')
os.chdir(abs_path)

search_words = set()
cur_success_files = set()
black_list_files = set()

while True:
    new_word = input('Введите слово,по которому будем совершать поиск (чтобы выйти введите y): ')
    if new_word == 'y':
        break

    search_words.add(new_word)

    for filename in glob('*.sql'):
        with open(filename, encoding='utf8') as sql_file:
            for word in search_words:
                if word in sql_file.read() and sql_file.name not in black_list_files:
                    cur_success_files.add(sql_file.name)
                else:
                    black_list_files.add(sql_file.name)
                    cur_success_files.discard(sql_file.name)

    pprint(cur_success_files)
    print('Всего: {}'.format(len(cur_success_files)))