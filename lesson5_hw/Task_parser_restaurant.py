cook_book = {}


def pars_data_restaurant():
    with open('DATA_FROM_RESTAURANT', encoding='utf8') as f:
        for line in f:
            dish_name = line.strip()
            cook_book[dish_name] = []
            f.readline()
            next_line = f.readline().strip()
            while next_line:
                ingr_name, quantity, measure = next_line.strip().split('|')
                cook_book[dish_name].append({'ingridient_name': ingr_name, 'quantity': quantity, 'measure': measure})
                next_line = f.readline().strip()


pars_data_restaurant()


def get_shop_list_by_dishes(dishes, person_count):
    necessery_ing = {}

    for dish in dishes:
        for ingridient in cook_book[dish]:
            ingr_name = ingridient['ingridient_name']
            measure = ingridient['measure']
            quantity = int(ingridient['quantity']) * person_count

            if ingr_name not in necessery_ing:
                necessery_ing[ingr_name] = {'quantity': quantity, 'measure': measure}
            else:
                quantity += necessery_ing[ingr_name]['quantity']
                necessery_ing[ingr_name]['quantity'] = quantity
    return necessery_ing


print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))