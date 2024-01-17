import tts
import os
import time
import pyautogui

from tools.json_work import read_json, write_json


def init_new_project():
    # Создаем новую директорию с начальными файлами
    projects_path = os.path.join('\\'.join(os.getcwd().split('\\')[:-1]), 'projects')

    data = read_json(f"{os.getcwd()}\const.json")

    cur_project_path = os.path.join(projects_path, f'project{data["last_project"] + 1}')
    os.mkdir(cur_project_path)
    data['last_project'] += 1
    write_json(f"{os.getcwd()}\const.json", data)

    with open(os.path.join(cur_project_path, 'main.py'), 'w+') as _:
        pass

    with open(os.path.join(cur_project_path, 'logs.txt'), 'w+') as _:
        pass

    x, y = pyautogui.locateCenterOnScreen("gui/wind.png")
    pyautogui.click(x, y)

    time.sleep(0.75)

    x, y = pyautogui.locateCenterOnScreen("gui/pycharm.png")
    pyautogui.click(x, y)

    time.sleep(1.5)
    while pyautogui.locateCenterOnScreen("gui/pycharm_loading_0.png") or pyautogui.locateCenterOnScreen(
            "gui/pycharm_loading_1.png"):
        continue

    time.sleep(3.5)  # Время загрузки skeletons

    # Открываем нужный проект
    x, y = pyautogui.locateCenterOnScreen("gui/file.png")
    pyautogui.click(x, y)
    time.sleep(0.5)

    x, y = pyautogui.locateCenterOnScreen("gui/open.png")
    pyautogui.click(x, y)
    time.sleep(1.5)

    pyautogui.press('esc')  # Защита от медленных HDD
    time.sleep(0.5)

    x, y = pyautogui.locateCenterOnScreen("gui/file.png")
    pyautogui.click(x, y)
    time.sleep(0.5)

    x, y = pyautogui.locateCenterOnScreen("gui/open.png")
    pyautogui.click(x, y)
    time.sleep(0.5)

    print(cur_project_path)
    pyautogui.hotkey('ctrl', 'alt', 'y')
    time.sleep(0.5)
    pyautogui.write(cur_project_path)
    time.sleep(5.5)

    x, y = pyautogui.locateCenterOnScreen('gui/ok.png')
    pyautogui.click(x, y)

    time.sleep(1.5)
    pyautogui.press('enter')
    time.sleep(3.5)

    # Настраиваем autosave
    try:
        pyautogui.hotkey('ctrl', 'alt', 's')
        time.sleep(1)

        try:
            x, y = pyautogui.locateCenterOnScreen('gui/pycharm_settings.png')
            pyautogui.click(x, y)
        except Exception:
            x, y = pyautogui.locateCenterOnScreen('gui/pycharm_setting_1.png')
            pyautogui.click(x, y)

        setting = pyautogui.locateOnScreen('gui/pycharm_autosave.png')
        pyautogui.click(setting[0] + 15, setting[1] + setting[-1] // 2)
        pyautogui.click(setting[0] + 250, setting[1] + setting[-1] // 2)

        pyautogui.hotkey('ctrl', 'a')
        pyautogui.press('1')

        time.sleep(0.5)
        x, y = pyautogui.locateCenterOnScreen('gui/apply.png')
        pyautogui.click(x, y)

    except Exception as e:
        print(e)
        time.sleep(1.5)
    pyautogui.press('esc')

    # Открываем main.py
    x, y = pyautogui.locateCenterOnScreen('gui/main.png')
    pyautogui.click(x, y, clicks=2)
    pyautogui.hotkey('ctrl', 'shift', 'f10')
    time.sleep(1)

    # Настраиваем logs
    try:
        x, y = pyautogui.locateCenterOnScreen('gui/conf.png')
        pyautogui.click(x, y)
        time.sleep(0.5)

        x, y = pyautogui.locateCenterOnScreen('gui/edit.png')
        pyautogui.click(x, y)
        time.sleep(1.5)

        x, y = pyautogui.locateCenterOnScreen('gui/logs.png')
        pyautogui.click(x, y)
        time.sleep(0.5)

        setting = pyautogui.locateOnScreen('gui/save_file.png')
        pyautogui.click(setting[0] + 15, setting[1] + setting[-1] // 2)
        pyautogui.click(setting[0] + 250, setting[1] + setting[-1] // 2)

        pyautogui.hotkey('ctrl', 'a')
        pyautogui.write(os.path.join(cur_project_path, 'logs.txt'))  # TODO: !!!

        time.sleep(0.5)
        x, y = pyautogui.locateCenterOnScreen('gui/apply_1.png')
        pyautogui.click(x, y)
    except Exception as e:
        print(e)
        pass

    pyautogui.press('esc')

    tts.va_speak('Инициализация прошла успешно!')


def open_project(idx: int):
    if read_json(f"{os.getcwd()}\const.json")["last_project"] < idx:
        tts.va_speak("Неверный проект")
        return

    try:
        x, y = pyautogui.locateCenterOnScreen("gui/wind.png")
        pyautogui.click(x, y)

        time.sleep(0.75)

        x, y = pyautogui.locateCenterOnScreen("gui/pycharm.png")
        pyautogui.click(x, y)

        time.sleep(1.5)
        while pyautogui.locateCenterOnScreen("gui/pycharm_loading_0.png") or pyautogui.locateCenterOnScreen(
                "gui/pycharm_loading_1.png"):
            continue

        time.sleep(3.5)  # Время загрузки skeletons
    except Exception:
        pyautogui.press('esc')
        time.sleep(1)

    # Открываем нужный проект
    x, y = pyautogui.locateCenterOnScreen("gui/file.png")
    pyautogui.click(x, y)
    time.sleep(0.5)

    x, y = pyautogui.locateCenterOnScreen("gui/open.png")
    pyautogui.click(x, y)
    time.sleep(1.5)

    pyautogui.press('esc')  # Защита от медленных HDD
    time.sleep(0.5)

    x, y = pyautogui.locateCenterOnScreen("gui/file.png")
    pyautogui.click(x, y)
    time.sleep(0.5)

    x, y = pyautogui.locateCenterOnScreen("gui/open.png")
    pyautogui.click(x, y)
    time.sleep(0.5)

    projects_path = os.path.join('\\'.join(os.getcwd().split('\\')[:-1]), 'projects')
    pyautogui.hotkey('ctrl', 'alt', 'y')
    time.sleep(0.5)

    pyautogui.write(os.path.join(projects_path, f'project{idx}'))
    time.sleep(5.5)

    x, y = pyautogui.locateCenterOnScreen('gui/ok.png')
    pyautogui.click(x, y)

    time.sleep(1.5)
    pyautogui.press('enter')
    time.sleep(3.5)


if __name__ == '__main__':
    time.sleep(3)
    init_new_project()
