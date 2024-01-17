import os
import yaml
from dotenv import load_dotenv

# Find .env file with os variables
load_dotenv("dev.env")

# Конфигурация
VA_NAME = 'BVA'
VA_VER = "0.1"
VA_ALIAS = ('компьютер',)

MICROPHONE_INDEX = -1

# Токен Picovoice
PICOVOICE_TOKEN = os.getenv('PICOVOICE_TOKEN')

# Path to PyCharm
PYCHARM_PATH = r'C:\Program Files\JetBrains\PyCharm Community Edition 2021.3.2\bin'
