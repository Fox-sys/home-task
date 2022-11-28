import json

DATA = json.load(open('2_settings.json', 'r'))


def search(word: str) -> str:
    for k, v in DATA.items():
        if v == word:
            return k


while (a := input()) != 'exit':
    print(search(a))
