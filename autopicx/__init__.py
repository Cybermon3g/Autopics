import logging 
from os import environ
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.network.connection.tcpabridged import ConnectionTcpAbridged

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.INFO)

API_ID = int(environ.get("API_ID", "28915632"))
API_HASH = environ.get("API_HASH", "19b37f365054be433a4d75e949ffde39")
SESSION = environ.get("1BVtsOGwBuxVnmiYaAx_3TWR_A5W9-RO9AehKUCoFEPZisrVdRjnwEFJzpPV-EcvoDGJAfPeZPeJmJnsM1_arMkbemTDtVbomsoB6LblXxwJLqN1FO09u-zinQtw4cjLd1hIBO7TQcrHfnZnS3kq0wC4imJj-5lJv9chJxl4akOhdHxml-XS8ZTjBgwVPO36kyT1CVkctIsumW-SYjzfJyL4T85Cre1XAoLuDO40IxlA7kfuL9GIXnJGwU44IVO1S504IIBNcflSPAqa3f0tTdiGWO-5b3mAgjmtJHoXq6khLBI_kY6VkKsvpgQ38vcBn6wqgm3WSSQzv9Zh0o7sVZFMmbZ-2P_M=")
TIME = int(environ.get("TIME", "60"))
CHANNEL_ID = int(environ.get("CHANNEL_ID", "-1001227879771"))


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

