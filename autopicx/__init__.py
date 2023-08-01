import logging 
from os import environ
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.network.connection.tcpabridged import ConnectionTcpAbridged

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.INFO)

API_ID = int(environ.get("API_ID", "28915632"))
API_HASH = environ.get("API_HASH", "19b37f365054be433a4d75e949ffde39")
SESSION = environ.get("1BVtsOI4Bu4zPirlq-DHNzV0AO9I9rY7flUfSUBaRfAqnxikgp4GJE9v3Np4KOo0lfG6QVh0S60tfzFoCq5XWJRqjnvLRPE28XEWnGaUDqQ3-JEWDo5onYP_4kMxs52AIfpvl_kjb4ZDqvTSD0XY1O6naL8uP2vCZRmSBHhtctkt_hD4bMY3P8fPwhWyFtdcIMOzm4--TX_jkam8iay4VHk9zFhbZ5yJeRvnP-mPgOSxi-4VZAV7lJct9KXbl-pzOZljvalPVgwZmnU9gVn_OEjpClh6_VboOvM4ORzO-d8oT8mhsJrFoOJBIHFTOrB2tOY7CK1EDWXFD1gyzJYfU2VUW8zEOMYk=")
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

