import os
import tts
from num2words import num2words
from transliterate import translit

data_to_change = {
    " ": 'пробел',
    ".": 'точка',
    ",": 'запятая',
    "-": 'минус',
    "\t": 'таб',
    "*": 'звездочка',
    "/": 'слэш',
    "%": 'процент',
    ":": 'двоеточие',
    '"': 'кавычка',
    "'": 'одинарная-кавычка',
    "(": 'открывающая-скобка',
    ")": 'закрывающая-скобка',
    "{": 'открывающая-фигурная-скобка',
    "}": 'закрывающая-фигурная-скобка',
    "=": 'равно',
    "+": 'плюс',
    "_": 'нижнее-подчеркивание',
    ">": 'больше',
    "<": 'меньше',
    "!": 'восклицательный-знак',
    "?": 'вопросительный знак'
}


def tell_all_file():
    with open("D:/Projects/BVA/projects/main.py", 'r', encoding='utf8') as file_py:  # TODO: Path
        file_to_read = file_py.read()

        for k, v in data_to_change.items():
            file_to_read = file_to_read.replace(k, ' ' + v + ' ')

        file_to_read = translit(file_to_read, 'ru')
    file_py.close()

    to_speak = ''
    for i, line in enumerate(file_to_read.split('\n')):
        words = line.split()
        for j in range(len(words)):
            if words[j].isnumeric():
                words[j] = num2words(words[j], lang='ru')
        print(f'Строка-{num2words(i + 1, lang="ru")}: ' + ' '.join(words) + ' конец-строки ')  # ОТЛАДКА
        to_speak += f'Строка-{num2words(i + 1, lang="ru")} ' + ' '.join(words) + ' конец-строки '
    print()

    tts.bva_speak(to_speak)


def tell_string_range(start: int, stop: int):
    with open("D:/Projects/BVA/projects/main.py", 'r', encoding='utf8') as file_py:  # TODO: Path
        file_to_read = file_py.read()

        for k, v in data_to_change.items():
            file_to_read = file_to_read.replace(k, ' ' + v + ' ')

        file_to_read = translit(file_to_read, 'ru')
    file_py.close()

    to_speak = ''
    for i, line in tuple(enumerate(file_to_read.split('\n')))[start - 1:stop]:
        words = line.split()
        for j in range(len(words)):
            if words[j].isnumeric():
                words[j] = num2words(words[j], lang='ru')
        print(f'Строка-{num2words(i + 1, lang="ru")}: ' + ' '.join(words) + ' конец-строки ')  # ОТЛАДКА
        to_speak += f'Строка-{num2words(i + 1, lang="ru")} ' + ' '.join(words) + ' конец-строки '
    print()

    tts.bva_speak(to_speak)


def read_console():
    with open("D:/Projects/BVA/projects/logs.txt", 'r', encoding='utf8') as file_py:  # TODO: Path
        file_to_read = file_py.read()

        for k, v in data_to_change.items():
            file_to_read = file_to_read.replace(k, ' ' + v + ' ')

        file_to_read = translit(file_to_read, 'ru')
    file_py.close()

    to_speak = ''
    for i, line in enumerate(file_to_read.split('\n')):
        words = line.split()
        for j in range(len(words)):
            if words[j].isnumeric():
                words[j] = num2words(words[j], lang='ru')
        print(f'Строка-{num2words(i + 1, lang="ru")}: ' + ' '.join(words) + ' конец-строки ')  # ОТЛАДКА
        to_speak += f'Строка-{num2words(i + 1, lang="ru")} ' + ' '.join(words) + ' конец-строки '
    print()

    tts.bva_speak(to_speak)


if __name__ == '__main__':
    tell_all_file()
