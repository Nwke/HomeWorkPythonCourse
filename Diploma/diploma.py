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


def main():
    investigated = '277079908'
    def_params = {
        'access_token': TOKEN_VK_API,
        'v': 5.80,
        'user_id': investigated,
        'extended': True,
    }
    group_params = {**def_params, 'fields': 'members_count'}

    investigated_friends = set(send_req(GET_FRIENDS, params=def_params).json()['response']['items'])
    investigated_groups = send_req(GET_GROUPS, params=group_params).json()['response']['items']

    investigated_groups_id = {group['id'] for group in investigated_groups}

    all_groups_friends = set()

    for friend in investigated_friends:
        print('Отправляем запрос..')
        try:
            group_friend = send_req(GET_GROUPS, params={
                'access_token': TOKEN_VK_API,
                'v': 5.80,
                'user_id': friend
            }).json()['response']['items']

            all_groups_friends.update(group_friend)
        except (KeyError, requests.exceptions.RequestException):
            pass
        time.sleep(1)

    succcess_groups_id = investigated_groups_id - all_groups_friends
    succes_groups = []

    for group in investigated_groups:
        if group['id'] in succcess_groups_id:
            succes_groups.append({
                'name': group['name'],
                'gid': group['id'],
                'members_count': group['members_count']
            })

    res = json.dumps(succes_groups, ensure_ascii=False)


main()
