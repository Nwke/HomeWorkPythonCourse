from collections import Counter
from pprint import pprint
import xml.etree.ElementTree as ET


def parse_news(file_name):

    tree = ET.parse(file_name)
    root = tree.getroot()
    freq_counter = Counter()

    for child_root in root[0]:
        for item in child_root:
            if item.tag == 'description':
                for word in item.text.split():
                    if len(word) > 6:
                        add_to_counter(freq_counter, word)

    freq_counter = sorted(freq_counter.items(), key=lambda x: x[1], reverse=True)

    for i in range(10):
        print(freq_counter.pop(0)[0])

    pprint('==== Файл обработан ====')

def add_to_counter(dict_counter, word):
    try:
        dict_counter[word] += 1
    except:
        dict_counter[word] = 1


need_proc_files = ['newsafr.xml', 'newsit.xml', 'newsfr.xml']

for file in need_proc_files:
    parse_news(file)