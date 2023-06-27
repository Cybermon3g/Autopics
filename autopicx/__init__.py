import logging 
from os import environ
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.network.connection.tcpabridged import ConnectionTcpAbridged

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.INFO)

API_ID = int(environ.get("API_ID", "28915632"))
API_HASH = environ.get("API_HASH", "19b37f365054be433a4d75e949ffde39")
SESSION = environ.get("1BVtsOHkBu4RV0njQhtH-NrK7TwAIl4HOK9nauwVKy5Boz-oFcf2-wfz2DyGMIt0cOIkl4VmEPp7tcPuF0cgcErRr7D3ClSiE7I1Y0XHiHs-ubfC4RIuNJ599h_8jkiMkEKfwUKsJ4YhBY-hipoGCasSEoKF6g30_RHZqZoRHNWWzvw4Ls_iTe0NAs_TRfvh87u9qLVLBdpM1zIYzXOUfkCS9m9BhVzV_Z4LDSuB0vvHtj3pdxNi9y2qHf2OYQIN4FUeHW233QvwZdJSc5vfQCiMFS3PKxD7uyKAwlGgh4haxFwfDYaNEsRR8fDMit4pX-rrYzI7rOZCUC8iVxhvh39zqSsnmm2g=")
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

