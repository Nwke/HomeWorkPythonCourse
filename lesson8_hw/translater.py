import requests
import json
import os
import glob

API_KEY = 'trnsl.1.1.20180726T173134Z.984a03fdc7308fb6.acd681f1a3aa09163e2123dfca633d3c00e8d1f2'
INIT_DATA_DIR = 'initial_data'
RES_DATA_DIR = 'res_data'
YANDEX_TRANSLATE_URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'


def get_text_from_file(file_path):
    with open(file_path, encoding='utf-8') as f:
        return f.read()


def create_result_file_translate(file_name, new_text):
    file_res_name = file_name[:file_name.find('.')] + '_res.txt'

    with open(file_res_name, 'w', encoding='utf-8') as file_res:
        file_res.write(new_text)


def get_translated_text(text_file, lang_to):
    try:
        params = {'key': API_KEY, 'text': text_file, 'lang': lang_to}
        response = requests.get(YANDEX_TRANSLATE_URL, params=params)

        return json.loads(response.text)['text'][0].strip()
    except:
        return 'TRNSLTE ERROR'


def translate_text(file_path, lang_to='ru'):
    text_file = get_text_from_file(file_path)
    text_translated = get_translated_text(text_file, lang_to)

    file_path = file_path.replace(INIT_DATA_DIR, RES_DATA_DIR)
    create_result_file_translate(file_path, text_translated)


# translate_text('DE.txt', 'de', 'ru')
# translate_text('ES.txt', 'es', 'ru')
# translate_text('FR.txt', 'fr', 'ru')

for file in glob.glob(f'{INIT_DATA_DIR}/*.txt'):
    translate_text(file)
