import logging 
from os import environ
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.network.connection.tcpabridged import ConnectionTcpAbridged

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.INFO)

API_ID = int(environ.get("API_ID", "28915632"))
API_HASH = environ.get("API_HASH", "19b37f365054be433a4d75e949ffde39")
SESSION = environ.get("1BVtsOHkBu4T1MnWRhDI4hB9NDIEGyuzVhJAtAdXps_1Pb3I4RY7RVCMTupy8GyYrGBQ16k9Zf3-aQyudPNKViF-7F2fhuaKjtIiEGb9C4jg0Qqrm4XkqOD-UpJ7BvNvJk6a-cVSXlP8jYnL6NsMvlHY-80m7_qEUPw5IduWdAQrz66pKZ-19UkKwEzZR7U1GmgwY02V8o7V2hGSkmDMUO7RMbZN1eTXxsMSaL2BAF_tzSC9U0YSn6TJTg02DUlQa_zbp6oc1RsvankLhAuhZPH-Afy09k3TVs4_p3-ENpL6DGCepaokCC2KZCHz-YW2kt2TvCaVAYweNHyfO8e7Gm5gIq9osaW8=")
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

