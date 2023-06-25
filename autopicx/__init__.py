import logging 
from os import environ
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.network.connection.tcpabridged import ConnectionTcpAbridged

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.INFO)

API_ID = int(environ.get("15762061"))
API_HASH = environ.get("364d3fa8f95aae815d62cf981ab1afe3")
SESSION = environ.get("1BVtsOGYBu0-hA3inzrawesjRpPhCTUrwPIpPaDnp6TEk7mqdJbvlrWxJJyYJTCJmRdLJ4eVz4ZuIpoGxR5nAJVXZSkzDgrV3y71OFWdKc74KgSotkFbHdxgfgCJOibdrjCd9O4FzR08o1uX66vvJ3iYmvMdAOq_Wiz3rKCdunuirR02a9sekUFElLhb70H562p2ruw9CBbIOjBMM-yOTxRUtIF8qP4k9DGWhq4mDWZ2jUaHIqK3maEBfblZPDICv5gMP6LY2dRV4yqM0X1f70AqQUDrG_vDmxbFVhwb0EcVjbo4_hrm12qQyMRNy4c8hKCDh8QaD99woc8lmg59EZe9Q6TCUqPY=")
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

