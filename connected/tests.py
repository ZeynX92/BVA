import time
import torch
import sounddevice as sd
from num2words import num2words
from transliterate import translit
from tts import va_speak, bva_speak

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
    "?": 'вопросительный знак',
    ";": 'точка-с-запятой',
    '[': 'открывающая-квадратная-скобка',
    ']': 'закрывающая-квадратная-скобка',
}


def tell_all_file(file_to_read: str, delta_bva: float = 0.5):
    for k, v in data_to_change.items():
        file_to_read = file_to_read.replace(k, ' ' + v + ' ')

    file_to_read = translit(file_to_read, 'ru')

    to_speak = ''
    for i, line in enumerate(file_to_read.split('\n')):
        words = line.split()
        for j in range(len(words)):
            if words[j].isnumeric():
                words[j] = num2words(words[j], lang='ru')
        # print(f'Строка-{num2words(i + 1, lang="ru")}: ' + ' '.join(words) + ' конец-строки ')  # ОТЛАДКА
        to_speak += f'Строка-{num2words(i + 1, lang="ru")} ' + ' '.join(words) + ' конец-строки '
    # print()

    if delta_bva == 0:
        va_speak(to_speak)
    else:
        bva_speak(to_speak, delta_bva)


if __name__ == '__main__':
    tests = [
        'print("Hello world!)',
        'print(87 + "90")',
        'var = int(input())\nif var\n  print()',
        'print(bon(9)[1:])',
        'def func()\n   return 15;',
    ]
    deltas = [0, 0.25, 0.5, 0.75]

    data = []
    for delta in deltas:
        print("=========================")
        tmp = []
        for i, test in enumerate(tests, 1):
            input(f"Нажмите Enter, чтобы приступить к ответу на вопрос {i}")

            start = time.time()
            tell_all_file(test, delta)
            input("Нажмите Enter, чтобы остановить таймер...\n")
            end = time.time()
            answer = input("Введите ответ испытуемого: ")
            time_delta = round(float(str(end - start)), 3)
            print(time_delta)

            tmp.append((answer, time_delta))
        data.append(tmp)

    with open('logs.txt', 'a', encoding='utf-8') as file:
        lines = []
        for i, delta in enumerate(deltas):
            lines.append(f'Задержка между словами: {delta} сек')

            for pair in data[i]:
                lines.append(f'Время: {pair[1]} --- Ответ: {pair[0]}')
            lines.append('=' * 24)

        file.writelines([line + '\n' for line in lines])
