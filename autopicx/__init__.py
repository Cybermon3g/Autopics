import logging 
from os import environ
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.network.connection.tcpabridged import ConnectionTcpAbridged

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.INFO)

API_ID = int(environ.get("API_ID", "28915632"))
API_HASH = environ.get("API_HASH", "19b37f365054be433a4d75e949ffde39")
SESSION = environ.get("1BVtsOIYBuwM4f9nSEMnNv5rY4-bFdD0HB5jPItYA0AcpQMSWflhjEw6OQEkb9l6xNMPLuoKTBxuJFBKXOCumADLAAvGXAlKtCfxww2Gxxc0KN8rbTzOU7-LsHcmDvYt_FkM5AW1Sn6pas08Pg-suwdOp1Ez2M5zot8EKMu9HGav9ifsEYmp69bLMPDKvVeAaMGp0Ex-UWWqgprE-PwNf5jZLvXOMIJfHyX7Dgbyk8uJ5YQG9mJNFBaiBX43pelIbsoogkg4OqHak_ANsE9NfgLptgNm44JSwUtYkJFL-duwVDQVh2t262mnQcwzzyUh6T6xpZsNys-GPI14qZCBRc5FTPzj-3us=")
TIME = int(environ.get("TIME", "60"))
CHANNEL_ID = int(environ.get("CHANNEL_ID", "-1001787823774"))


if SESSION is not None:
    session = StringSession(str(SESSION))
else:
    session = "pyrobot"

try:
    client = TelegramClient(
        session=session,
        api_id=API_ID,
        api_hash=API_HASH,
        connection=ConnectionTcpAbridged
    )
    client.start()
    
except Exception as e:
    print(e)

