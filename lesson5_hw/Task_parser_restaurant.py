from pprint import pprint
CURRENT_FILE = 'DATA_FROM_RESTAURANT.txt'


def get_cook_book_restaurant(file):
    cook_book = {}

    with open(file, encoding='utf8') as f:
        for line in f:
            dish_name = line.strip()
            cook_book[dish_name] = []
            f.readline()
            next_line = f.readline().strip()
            while next_line:
                ingr_name, quantity, measure = list(map(str.strip, next_line.split('|')))
                cook_book[dish_name].append({'ingridient_name': ingr_name, 'quantity': quantity, 'measure': measure})
                next_line = f.readline().strip()

    return cook_book


def get_shop_list_by_dishes(dishes, person_count, cook_book):
    necessery_ing = {}

    for dish in dishes:
        for ingridient in cook_book[dish]:
            ingr_name = ingridient['ingridient_name']
            measure = ingridient['measure']
            quantity = int(ingridient['quantity']) * person_count

            if ingr_name not in necessery_ing:
                necessery_ing[ingr_name] = {'quantity': quantity, 'measure': measure}
            else:
                necessery_ing[ingr_name]['quantity'] += quantity
    return necessery_ing


pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2, get_cook_book_restaurant(CURRENT_FILE)))
