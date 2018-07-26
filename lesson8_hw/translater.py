import requests
import json
import os

init_data_path = os.path.join(os.path.abspath(''), 'initial_data')
res_data_path = os.path.join(os.path.abspath(''), 'res_data')
API_KEY = 'trnsl.1.1.20180726T173134Z.984a03fdc7308fb6.acd681f1a3aa09163e2123dfca633d3c00e8d1f2'


def translate_text(path_from, path_to, lang_from, lang_to='ru'):
    with open(os.path.join(init_data_path, path_from), encoding='utf-8') as old_file:
        text_file = old_file.read()

    response = requests.get(('https://translate.yandex.net/api/v1.5/tr.json/'
                             'translate?key={0}&text={1}&lang={2}-{3}'.format(API_KEY, text_file, lang_from, lang_to)))
    new_text = json.loads(response.text)['text'][0].strip()

    with open(os.path.join(res_data_path, path_to), 'w', encoding='utf-8') as file_res:
        file_res.write(new_text)


translate_text('DE.txt', 'DE_res.txt', 'de', 'ru')
translate_text('ES.txt', 'ES_res.txt', 'es', 'ru')
translate_text('FR.txt', 'FR_res.txt', 'fr', 'ru')
