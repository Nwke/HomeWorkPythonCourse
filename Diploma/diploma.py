import requests
import time
import requests.exceptions
import json
from pprint import pprint

TOKEN_VK_API = '7b23e40ad10e08d3b7a8ec0956f2c57910c455e886b480b7d9fb59859870658c4a0b8fdc4dd494db19099'
SERVICE_TOKEN = '4d28efa04d28efa04d28efa0a74d4d8cf844d284d28efa016464fcfc0449c661afd0bbe'

GET_GROUPS = 'groups.get'
GET_FRIENDS = 'friends.get'


def send_req(method, params):
    return requests.get(f'https://api.vk.com/method/{method}', params=params)


def process_param(user_id, params, extended, add_params):
    add_params = {} if add_params is None else add_params
    if params is None:
        params = {
            'access_token': TOKEN_VK_API,
            'v': 5.80,
            'user_id': user_id,
            'extended': extended
        }
    try:
        int(user_id)
        params['user_id'] = user_id
    except ValueError:
        params['screen_name'] = user_id

    params.update(add_params)
    return params


def get_groups(user_id, params=None, extended=0, add_params=None):
    params = process_param(user_id, params, extended, add_params)
    return send_req(GET_GROUPS, params=params).json()['response']['items']


def get_friends(user_id, params=None, extended=0, add_params=None):
    params = process_param(user_id, params, extended, add_params)
    return send_req(GET_FRIENDS, params=params).json()['response']['items']


def main():
    investigated = input('Введите ник или id для обработки: ')
    permissible_friend = int(input('Введите допустимое количество друзей в группах'))

    investigated_friends = set(get_friends(investigated))
    investigated_groups = get_groups(investigated, extended=True, add_params={'fields': 'members_count'})

    investigated_groups_id = {group['id'] for group in investigated_groups}

    all_groups_friends = set()

    count_friend = len(investigated_friends)
    
    for friend in investigated_friends:
        print(f'Осталось обработать {count_friend} друзей')
        print('Отправляем запрос...')

        try:
            group_friend = get_groups(friend)
            all_groups_friends.update(group_friend)

        except (KeyError, requests.exceptions.RequestException):
            pass

        finally:
            count_friend -= 1
            time.sleep(0.5)

    print('Подготавливаем результат...')

    succcess_groups_id = investigated_groups_id - all_groups_friends
    succes_groups = []

    for group in investigated_groups:
        if group['id'] in succcess_groups_id:
            succes_groups.append({
                'name': group['name'],
                'gid': group['id'],
                'members_count': group['members_count']
            })

    with open('groups.json', 'w+', encoding='utf8') as res_file:
        json.dump(succes_groups, res_file, ensure_ascii=False, indent=2)

    print('Результат работы в файле groups.json')


main()
