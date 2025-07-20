# Add your details here and then deploy by clicking on HEROKU Deploy button
from os import environ

API_ID = int(environ.get("API_ID", "22727464"))
API_HASH = environ.get("API_HASH", "f0e595a263c89aa17f6571b8af296ced")
BOT_TOKEN = environ.get("BOT_TOKEN", "7110231022:AAHzjuE3MR7FdUvdFnaEHKurmQ9526aTIiM")

# Sudo Users Configuration
SUDO_USERS = list(map(int, environ.get("SUDO_USERS", "887699812").split(","))) if environ.get("SUDO_USERS", "") else []

# Admin Configuration - Has FULL and PERMANENT access
ADMIN_USERS = list(map(int, environ.get("ADMIN_USERS", "887699812").split(","))) if environ.get("ADMIN_USERS", "") else []
