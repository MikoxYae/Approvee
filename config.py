import os
from typing import List

API_ID = os.environ.get("API_ID", "28614709")
API_HASH = os.environ.get("API_HASH", "f36fd2ee6e3d3a17c4d244ff6dc1bac8")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7938087417:AAHlOKaw_XPTlfET_qwfq2USmnFsJaKi5gA")
ADMIN = int(os.environ.get("ADMIN", "7534267467"))
PICS = (os.environ.get("PICS", "https://graph.org/file/075bbc8002a19e76d99b5-59bcbc49f2d7c2e0b5.jpg")).split()

LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", ""))
NEW_REQ_MODE = os.environ.get("NEW_REQ_MODE", "True").lower() == "true"  # Set "True" For accept new requests

DB_URI = os.environ.get("DB_URI", "mongodb+srv://ZeroTwo:aloksingh@zerotwo.3q3ij.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DB_NAME", "Approve")

IS_FSUB = os.environ.get("IS_FSUB", "False").lower() == "true"  # Set "True" For Enable Force Subscribe
AUTH_CHANNELS = list(map(int, os.environ.get("AUTH_CHANNEL", "").split())) # Add Multiple channel ids
