import requests
from pprint import pprint

TOKEN = 'f154592cca004b01f8cd886a3a92c761f1869e7bcb803f89b5e5f6cc4371e3d778b335d5c5d396aedd976'
SERVICE_KEY = 'b482e1c8b482e1c8b482e1c8ceb4e78290bb482b482e1c8efd80a7a459ea5c1578870e3'


class User:
    def __init__(self, id, first_name, last_name, token):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.token = token

    def __repr__(self):
        return 'https://vk.com/id' + str(self.id)

    def __and__(self, other):
        mutual_friends = self.friends() & other.friends()
        l = []
        for user in mutual_friends:
            try:
                l.append(User(
                    **UserInterface.get_user(user)['response'][0],
                    token=SERVICE_KEY
                ))
            except TypeError:
                pass
        return l

    def request(self, method, _params=None):
        _params = {} if _params is None else _params

        params = {
            'access_token': self.token,
            'v': 5.80,
            'user_id': self.id
        }
        params.update(_params)

        return requests.get(
            'https://api.vk.com/method/{}'.format(method),
            params=params
        )

    @property
    def status(self):
        response = self.request('status.get')
        return response.json()['response']['text']

    def friends(self, ):
        response = self.request('friends.get')
        return set(response.json()['response']['items'])

    def set_status(self, text):
        response = requests.get(
            'https://api.vk.com/method/status.set',
            params=dict(
                access_token=self.token,
                v=5.80,
                text=text
            ))
        return response.json()['response']

    def get_mutual_friends(self, other):
        return self.__and__(other)

    def x(self):
        return self.request('friends.get', _params={'access_token': SERVICE_KEY, 'user_id': self.id, 'v': 5.80})


class UserInterface:
    @staticmethod
    def get_user(user_id):
        return requests.get(
            'https://api.vk.com/method/users.get',
            params={'access_token': SERVICE_KEY, 'user_ids': user_id, 'v': 5.80}).json()


response_get_users = requests.get(
    'https://api.vk.com/method/users.get',
    params=dict(
        access_token=TOKEN,
        v=5.80,

    ))

user_denis = User(
    **response_get_users.json()['response'][0],
    token=TOKEN
)

user_vlad = User(
    **UserInterface.get_user('179371221')['response'][0],
    token=SERVICE_KEY
)

if __name__ == 'main':
    print(len(user_denis.friends()))
    print(len(user_vlad.friends()))

    mut_friends = user_vlad.get_mutual_friends(user_denis)
    print(len(mut_friends), mut_friends)
