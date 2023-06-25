import logging 
from os import environ
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.network.connection.tcpabridged import ConnectionTcpAbridged

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.INFO)

API_ID = int(environ.get("API_ID", "28915632"))
API_HASH = environ.get("API_HASH", "19b37f365054be433a4d75e949ffde39")
SESSION = environ.get("1BVtsOGwBu3oSY5v04T3O9s8jssGknT1dE2ditImHmpz9h18PNr6oY89vZWu-iDIU95PPzH4cK9VUjmCI5dVjDkDZIsN-hvaWfDAnvsyrsGOr7PsPYOc4HTIAxe4Kk_pXxrbPpCgJSxj8VjKDCFxnvT9_TL1mt-Ng5fTHYLHonn-RAdRF_l7JrsDH_ESQwsTHOgnGmkITkcOUyUHvMCO3yLEvRJpTgT1tmB8CAgS7Ryll9e0XAzE58hU7ZuARzJybSeEBFrEdkHqLuwJRveCK1DxRmBlOUKnkM6o4ZHohsZIEddEx3jPktO_A6g8rOhV5qUoh1oUB3Lc63wwxGIsXgZ-L50Bs9sI=")
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

