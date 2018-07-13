from DATA import directories, documents


def print_name():
    doc_number = input('Введите номер документа: ')
    for doc in documents:
        if doc['number'] == doc_number:
            print(doc['name'])


def print_documents():
    for doc in documents:
        print('{} "{}" "{}" '.format(doc['type'], doc['number'], doc['name']))


def print_regiment():
    doc_number = input('Введите номер документа: ')
    for directory, content in directories.items():
        if doc_number in content:
            print(directory)


def add_directory():
    number, type, name, number_directory = input('Введите данные').split()
    item = {'type': type, 'number': number, 'name': name}
    directories[number] = item


def delete_doc():
    doc_num = input('Введите номер документы: ')
    for doc in documents:
        if doc['number'] == doc_num:
            documents.remove(doc)
    for regiment, cont in directories.items():
        if doc_num in cont:
            cont.remove(doc_num)


def move_doc():
    doc_number = input('Введите номер документа: ')
    to_regiment = input('Введите полку,на которую надо переместить: ')
    for regiment, cont in directories.items():
        if doc_number in cont:
            cont.remove(doc_number)
    directories[to_regiment].append(doc_number)


def add_regiment():
    numb_regiment = input('Введите номер полки,которую надо добавить: ')
    directories[numb_regiment] = []


while True:
    command = str.lower(input('Введите команду: '))
    if command == 'p':
        print_name()
    elif command == 'l':
        print_documents()
    elif command == 's':
        print_regiment()
    elif command == 'a':
        add_directory()
    elif command == 'd':
        delete_doc()
    elif command == 'm':
        move_doc()
    elif command == 'as':
        add_regiment()