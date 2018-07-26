from collections import Counter
from pprint import pprint
import json
import codecs
import os

os.chdir('data')


need_proc_files = ['newsafr.json', 'newsit.json', 'newsfr.json']
encoding = ['utf-8', 'utf-16', 'GBK', 'windows-1251', 'ASCII']


def check_enc(filename):
    for enc in encoding:
        try:
            open(filename, encoding=enc).read()
        except (UnicodeDecodeError, LookupError):
            pass
        else:
            return enc


def parse_news(file_name: str) -> None:
    enc = check_enc(file_name)
    with codecs.open(file_name, encoding=enc) as json_file:
        news = json.load(json_file)

    articles = news['rss']['channel']['items']
    freq_counter = Counter()

    for article in articles:
        for word in article['description'].split():
            if len(word) > 6:
                add_to_counter(freq_counter, word)

    freq_counter = sorted(freq_counter.items(), key=lambda x: x[1], reverse=True)

    for i in range(10):
        print(freq_counter.pop(0)[0])

    pprint('==== Файл {} обработан ===='.format(file_name))


def add_to_counter(dict_counter: dict, word: str) -> None:
    try:
        dict_counter[word] += 1
    except:
        dict_counter[word] = 1


for file in need_proc_files:
    parse_news(file)