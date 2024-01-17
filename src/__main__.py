# Внешние модули
import os
import json
import vosk
import time
import yaml
import struct
import pyautogui
import pvporcupine
from fuzzywuzzy import fuzz
from pvrecorder import PvRecorder
from words2numsrus import NumberExtractor

# Внутренние модули
import config
import tts
from commands.go_to import go_to
from commands.setup import init_new_project, open_project
from commands.tell_file import tell_all_file, tell_string_range, read_console

CDIR = os.getcwd()
VA_CMD_LIST = yaml.safe_load(open('commands.yaml', 'rt', encoding='utf8'))

porcupine = pvporcupine.create(access_key=config.PICOVOICE_TOKEN, keywords=['computer'], sensitivities=[1])

# VOSK
model = vosk.Model("model_small")
samplerate = 16000
device = config.MICROPHONE_INDEX
kaldi_rec = vosk.KaldiRecognizer(model, samplerate)

extractor = NumberExtractor()


def va_respond(voice: str):
    global recorder, message_log, first_request
    print(f"Распознано: {voice}")

    cmd = recognize_cmd(filter_cmd(voice))
    print(cmd)

    message_log = voice

    if len(cmd['cmd'].strip()) <= 0:
        return False
    elif cmd['percent'] < 70 or cmd['cmd'] not in VA_CMD_LIST.keys():
        tts.va_speak("Не понял Вас...")
    else:
        execute_cmd(cmd['cmd'])
        return True


def filter_cmd(raw_voice: str):
    cmd = raw_voice

    for x in config.VA_ALIAS:
        cmd = cmd.replace(x, "").strip()

    cmd = extractor.replace_groups(cmd)

    return cmd


def recognize_cmd(cmd: str):
    rc = {'cmd': '', 'percent': 0}
    for c, v in VA_CMD_LIST.items():
        for x in v:
            vrt = fuzz.ratio(cmd, x)
            if vrt > rc['percent']:
                rc['cmd'] = c
                rc['percent'] = vrt

    return rc


def execute_cmd(cmd: str):
    """Исполнитель команд"""
    global message_log
    if cmd == 'tell_all_file':
        pyautogui.hotkey('ctrl', 's')
        tell_all_file()
    elif cmd == 'tell_string_range':
        try:
            pyautogui.hotkey('ctrl', 's')
            data = extractor.replace_groups(message_log)
            start, stop = [int(i) for i in data.split() if i.isdigit()]
            tell_string_range(start, stop)
        except Exception:
            tts.va_speak("Не понял Вас")
    elif cmd == 'tell_string':
        try:
            pyautogui.hotkey('ctrl', 's')
            data = extractor.replace_groups(message_log)
            start = [int(i) for i in data.split() if i.isdigit()][0]
            tell_string_range(start, start)
        except Exception:
            tts.va_speak("Не понял Вас")
    elif cmd == 'run_project_main_file':
        pyautogui.hotkey('ctrl', 'shift', 'F10')
    elif cmd == 'stop_project_main_file':
        pyautogui.hotkey('ctrl', 'F2')
    elif cmd == 'init_new_project':
        init_new_project()
    elif cmd == 'go_to':
        try:
            pyautogui.hotkey('ctrl', 's')
            data = extractor.replace_groups(message_log)
            start = [int(i) for i in data.split() if i.isdigit()][0]
            go_to(start)
        except Exception as e:
            print(e)
            tts.va_speak("Не понял Вас")
    elif cmd == 'read_console':
        read_console()
    elif cmd == 'open_project':
        data = extractor.replace_groups(message_log)
        start = [int(i) for i in data.split() if i.isdigit()][0]
        open_project(start)


recorder = PvRecorder(device_index=config.MICROPHONE_INDEX, frame_length=porcupine.frame_length)
recorder.start()
print('Using device: %s' % recorder.selected_device)  # ОТЛАДКА

print(f"В.И.К. (v3.0) начал свою работу ...")  # ОТЛАДКА
time.sleep(0.5)

ltc = time.time() - 1000

while True:
    try:
        pcm = recorder.read()
        keyword_index = porcupine.process(pcm)

        if keyword_index >= 0:
            # Если услышали слово-отклик
            recorder.stop()
            print("Yes, sir.")
            recorder.start()
            ltc = time.time()

        while time.time() - ltc <= 10:
            pcm = recorder.read()
            sp = struct.pack("h" * len(pcm), *pcm)

            if kaldi_rec.AcceptWaveform(sp):
                if va_respond(json.loads(kaldi_rec.Result())["text"]):
                    ltc = time.time()

                break

    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")  # ОТЛАДКА
        raise
