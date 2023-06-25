import logging 
from os import environ
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.network.connection.tcpabridged import ConnectionTcpAbridged

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.INFO)

API_ID = int(environ.get("API_ID", "15762061"))
API_HASH = environ.get("API_HASH", "364d3fa8f95aae815d62cf981ab1afe3")
SESSION = environ.get("1BVtsOGwBu2svQmlU-q2e-EJ9gNLYCAdUHwBc788_KZQZFlSStYfwwxQ_oy0z79d3laJi8QJ8p_D2xpa4xNogl36dRsd8tB0omlavAFlCbuxySTOzWkWmBQYbCaXs7hLygOq-j0NqqCXur_YxCumfgdE5cSB5d5sB7rlL3i7s1eRo-Uk_7fqcyfyffHe3uTxzP946QOzjrbdWA86ZmmTwEEI200EKl89_x31Zz6-Da80VlmbREUt2Qyet97XszWRGIRRlRyJ4liZJ-FegiWCT07aSig5npzwo_E3YrciCiigL_IaNJ4Ivyqy9xJLnpIjUq-dUUX6ZIiZ5HCCTQCbuLcUeEThDDcg=")
TIME = int(environ.get("TIME", "60"))
CHANNEL_ID = int(environ.get("CHANNEL_ID", "-1001900598149"))


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

