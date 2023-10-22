import os

API_ID = API_ID = 22871928

API_HASH = os.environ.get("API_HASH", "b6471e2cf230e5dea0e68faa0ab626d2")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6654605912:AAFy2Js6kiwUq1a18pt3O5zPReCAHEw9XPE")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 6621567329)) 

LOG = -1001851582041

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "6621567329 6190740811").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


