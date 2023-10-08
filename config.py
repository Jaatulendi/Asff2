import os

API_ID = API_ID = 20088962

API_HASH = os.environ.get("API_HASH", "257f47d347157555890a64b12bc0134f")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6068322326:AAGUyoxWjLlMDuv1HbtutlgXU3E01U3eVp0")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 6137253423))

LOG = -1001784009370

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "6137253423 6190740811").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


