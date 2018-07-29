import requests
import json
import os

API_KEY = 'trnsl.1.1.20180726T173134Z.984a03fdc7308fb6.acd681f1a3aa09163e2123dfca633d3c00e8d1f2'
INIT_DATA_PATH = os.path.join(os.path.abspath(''), 'initial_data')
RES_DATA_PATH = os.path.join(os.path.abspath(''), 'res_data')


def get_text_from_file(file_name):
    with open(os.path.join(INIT_DATA_PATH, file_name), encoding='utf-8') as f:
        return f.read()


def create_result_file_translate(file_name, new_text):
    file_res_name = file_name[:file_name.find('.')] + '_res.txt'

    with open(os.path.join(RES_DATA_PATH, file_res_name), 'w', encoding='utf-8') as file_res:
        file_res.write(new_text)


def get_translated_text(text_file, lang_from, lang_to):
    response = requests.get(('https://translate.yandex.net/api/v1.5/tr.json/'
                             'translate?key={0}&text={1}&lang={2}-{3}'.format(API_KEY, text_file, lang_from, lang_to)))
    return json.loads(response.text)['text'][0].strip()


def translate_text(file_name, lang_from, lang_to='ru'):
    text_file = get_text_from_file(file_name)
    text_translated = get_translated_text(text_file, lang_from, lang_to)
    create_result_file_translate(file_name, text_translated)


translate_text('DE.txt', 'de', 'ru')
translate_text('ES.txt', 'es', 'ru')
translate_text('FR.txt', 'fr', 'ru')
