# This file is a part of TG-FileStreamBot
# Coding : Jyothis Jayanth [@EverythingSuckz]

import sys
from os import environ
from dotenv import load_dotenv

load_dotenv()


class Var(object):
    MULTI_CLIENT = False
    API_ID = int(getenv("API_ID", "26305247"))
    API_HASH = str(getenv("API_HASH",  "20ca7e6687c281e11782856c7efd0ff7"))
    BOT_TOKEN = str(getenv("BOT_TOKEN", "6257817586:AAHiHfYz_Ykn_n1QHgE7o1aRdOn5Gxg6M4U"))
    SLEEP_THRESHOLD = int(environ.get("SLEEP_THRESHOLD", "60"))  # 1 minte
    WORKERS = int(environ.get("WORKERS", "6"))  # 6 workers = 6 commands at once
    BIN_CHANNEL = int(
        environ.get("BIN_CHANNEL", "-1001853354560")
    )  # you NEED to use a CHANNEL when you're using MULTI_CLIENT
    PORT = int(environ.get("PORT", 443))
    BIND_ADDRESS = str(environ.get("WEB_SERVER_BIND_ADDRESS", "178.128.207.223"))
    PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
    HAS_SSL = str(environ.get("HAS_SSL", "True").lower()) in ("1", "true", "t", "yes", "y")
    NO_PORT = str(environ.get("NO_PORT", "0").lower()) in ("1", "true", "t", "yes", "y")
    HASH_LENGTH = int(environ.get("HASH_LENGTH", 6))
    if not 5 < HASH_LENGTH < 64:
        sys.exit("Hash length should be greater than 5 and less than 64")
    FQDN = str(environ.get("FQDN", BIND_ADDRESS))
    URL = "http{}://{}{}/".format(
            "s" if HAS_SSL else "", FQDN, "" if NO_PORT else ":" + str(PORT)
        )
    KEEP_ALIVE = str(environ.get("KEEP_ALIVE", "0").lower()) in  ("1", "true", "t", "yes", "y")
    DEBUG = str(environ.get("DEBUG", "0").lower()) in ("1", "true", "t", "yes", "y")
    USE_SESSION_FILE = str(environ.get("USE_SESSION_FILE", "0").lower()) in ("1", "true", "t", "yes", "y")
    ALLOWED_USERS = [x.strip("@ ") for x in str(environ.get("ALLOWED_USERS", "") or "").split(",") if x.strip("@ ")]
