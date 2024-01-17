import time
import tts
import pyautogui
from num2words import num2words


def go_to(idx: int):
    pyautogui.hotkey('ctrl', 'home')

    for i in range(idx - 1):
        pyautogui.press('down')
    with open("D:/Projects/BVA/projects/main.py", 'r', encoding='utf8') as file_py:  # TODO: Path
        file_to_read = file_py.read()
        size = len(file_to_read.split('\n'))

    if size >= idx:
        tts.va_speak(f'Вы находитесь на строке {num2words(idx, lang="ru")}')
    else:
        tts.va_speak(f'Вы находитесь на строке {num2words(size, lang="ru")}')
