import requests
import time
import requests.exceptions
import json
import config
import VK_API

TOKEN_VK_API = config.TOKEN_VK_API

GET_GROUPS = VK_API.GET_GROUPS
GET_FRIENDS = VK_API.GET_FRIENDS
IS_MEMBER = VK_API.IS_MEMBER

RESTRICT_IS_MEMBER = config.RESTRICT_IS_MEMBER


def send_req(method, user_id=None, params=None, extended=0, add_params=None):
    params = process_param(user_id, params, extended, add_params)
    req = requests.get(f'https://api.vk.com/method/{method}', params=params).json()

    if 'error' in req and req['error']['error_code'] == 6:
        time.sleep(2)
        while 'error' in req and req['error']['error_code'] == 6:
            req = requests.get(f'https://api.vk.com/method/{method}', params=params).json()
            time.sleep(2)
        return req

    return req


def process_param(user_id, params, extended=0, add_params=None):
    add_params = {} if add_params is None else add_params
    if params is None:
        params = {
            'access_token': TOKEN_VK_API,
            'v': 5.80,
            'extended': extended
        }
    if user_id is not None:
        try:
            int(user_id)
            params['user_id'] = user_id
        except ValueError:
            params['screen_name'] = user_id

    params.update(add_params)
    return params


def get_groups(user_id, params=None, extended=0, add_params=None):
    req = send_req(GET_GROUPS, user_id, params, extended, add_params)
    return req['response']['items']


def get_friends(user_id, params=None, extended=0, add_params=None):
    req = send_req(GET_FRIENDS, user_id, params, extended, add_params)
    return req['response']['items']


def is_members(add_params):
    req = send_req(IS_MEMBER, add_params=add_params)
    return req['response']


def form_success_groups(investigated_groups, success_groups_id):
    success_groups = []

    for group in investigated_groups:
        if group['id'] in success_groups_id and 'deactivated' not in group and group['is_closed'] != 1:
            success_groups.append({
                'name': group['name'],
                'gid': group['id'],
                'members_count': group['members_count']
            })

    return success_groups


def write_res_to_file(file, data):
    with open(file, 'w+', encoding='utf8') as file_result:
        json.dump(data, file_result, ensure_ascii=False, indent=2)


def main():
    investigated = input('Введите ник или id для обработки: ')
    permissible_friend = int(input('Введите допустимое количество друзей в группах: '))

    investigated_friends = list(map(str, get_friends(investigated)))
    investigated_groups = get_groups(investigated, extended=1, add_params={'fields': 'members_count'})

    investigated_groups_id = {group['id'] for group in investigated_groups}

    success_groups_id = []

    for investigated_group in investigated_groups_id:
        print('Отправляем запрос...')
        curr_users_in_group = 0
        remaining_users = investigated_friends.copy()

        while remaining_users:
            users_id = ','.join(remaining_users[:RESTRICT_IS_MEMBER])
            remaining_users = remaining_users[RESTRICT_IS_MEMBER:]

            add_params = {
                'user_ids': users_id,
                'group_id': str(investigated_group)
            }

            members = is_members(add_params=add_params)

            # obj_member['member'] stores 0 or 1
            # => are person in group or not
            for obj_member in members:
                curr_users_in_group += obj_member['member']

        if permissible_friend - curr_users_in_group >= 0:
            success_groups_id.append(investigated_group)

    print('Подготавливаем результат..')

    success_groups = form_success_groups(investigated_groups, success_groups_id)

    write_res_to_file('groups.json', success_groups)
    print('Результат работы в файле groups.json')


if __name__ == '__main__':
    main()
