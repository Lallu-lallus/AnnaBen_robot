import re
from os import environ
id_pattern = re.compile(r'^.\d+$')


# Bot information
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ['API_ID'])
API_HASH = environ['API_HASH']
BOT_TOKEN = environ['BOT_TOKEN']

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', False))
PICS = (environ.get('PICS', 'https://telegra.ph/file/96438c4d4c4b9a78505b9.jpg https://telegra.ph/file/e37fcf0c532b95a8dfb91.jpg https://telegra.ph/file/5fc1c6e2fdcd41db1772a.jpg https://telegra.ph/file/753fe4a57ed3934caa194.jpg https://telegra.ph/file/36b0d543462f2d5ffc6e9.jpg https://telegra.ph/file/6327ef11e0b1f70704364.jpg https://telegra.ph/file/18f12eeba6fcf227d32d6.jpg https://telegra.ph/file/2365b1e360a1567491f41.jpg https://telegra.ph/file/d586cf7341cb3610da734.jpg https://telegra.ph/file/a9c8adab2dbe5f7bacd96.jpg https://telegra.ph/file/fd73ebab5b4199d693819.jpg https://telegra.ph/file/8b08a62f850f8f75d88ac.jpg https://telegra.ph/file/55f2bfebb38f8b98c03cc.jpg https://telegra.ph/file/d2718a5299a1e20f3ac9f.jpg https://telegra.ph/file/45c60ced4510b16c1e769.jpg')).split()

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', "").split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('AUTH_CHANNEL')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else auth_channel
AUTH_GROUPS = [int(admin) for admin in environ.get("AUTH_GROUPS", "").split()]

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "")
DATABASE_NAME = environ.get('DATABASE_NAME', "Rajappan")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1001524777973'))
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'TeamEvamaria')

CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", None)
