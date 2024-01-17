import time
import torch
import sounddevice as sd

language = 'ru'
model_id = 'ru_v3'
sample_rate = 48000  # 48000
speaker = 'aidar'  # aidar, baya, kseniya, xenia, random
put_accent = True
put_yo = True
device = torch.device('cpu')

model, _ = torch.hub.load(repo_or_dir='snakers4/silero-models', model='silero_tts', language=language, speaker=model_id)
model.to(device)


# воспроизводим
def va_speak(what: str):
    audio = model.apply_tts(text=what + "..", speaker=speaker, sample_rate=sample_rate, put_accent=put_accent,
                            put_yo=put_yo)

    sd.play(audio, sample_rate * 0.95)  # 1.05
    time.sleep((len(audio) / sample_rate) + 0.5)
    sd.stop()


def bva_speak(what: str, delta: float = 0.5):
    data = what.split()

    for word in data:
        va_speak(word.replace('-', ' '))
        time.sleep(delta)
