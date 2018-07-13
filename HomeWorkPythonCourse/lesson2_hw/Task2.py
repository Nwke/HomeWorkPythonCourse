import csv

ID = 0
ROOMS = 1
TYPE = 2
PRICE = 11

flats_list = list()

with open('output.csv', newline='') as csvfile:
    flats_csv = csv.reader(csvfile, delimiter=';')
    flats_list = list(flats_csv)

# можете посмотреть содержимое файла с квартирами через print, можете - на вкладке output.csv
# print (flats_list)


# TODO 1:
# 1) Напишите цикл, который проходит по всем квартирам, и показывает только новостройки
# и их порядковые номера в файле. Подсказка - вам нужно изменить этот код:
count_new = 0
for ind, flat in enumerate(flats_list):
    if "новостройка" in flat:
        count_new += 1
        # print("{}, порядковый номер {}".format(flat, ind))
print('Всего новостроек: ' + str(count_new))
# 2) добавьте в код подсчет количества новостроек


# TODO 2:
# 1) Сделайте описание квартиры в виде словаря, а не списка. Используйте следующие поля из файла output.csv: ID,
# Количество комнат;Новостройка/вторичка, Цена (руб). У вас должно получиться примерно так:
current_flat = flats_list[5]
flat_info = {"id": current_flat[ID], "rooms": current_flat[ROOMS], "type": current_flat[TYPE], "price": current_flat[PRICE]}

# 2) Измените код, который создавал словарь для поиска квартир по метро так,
#  чтобы значением словаря был не список ID квартир, а список описаний квартир в виде словаря, который вы сделали в п.1
subway_dict = {}
for flat in flats_list:
    subway = flat[3].replace("м.", "")
    flat_info = {"id": flat[ID], "rooms": flat[ROOMS], "type": flat[TYPE], "price": flat[PRICE]}
    if subway not in subway_dict.keys():
        subway_dict[subway] = list()
    subway_dict[subway].append(flat_info)
# print(subway_dict)

# 3) Самостоятельно напишите код, который подсчитываети выводит, сколько квартир нашлось у каждого метро.
for station, apartments in subway_dict.items():
    print('У станции {} находится {} квартир'.format(station, len(apartments)))
