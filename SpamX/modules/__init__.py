from SpamX.config import *
from SpamX.core.version import __version__
from SpamX import sudoser, RiZoeL 
from RiZoeLX import __version__ as pip_vr
from pyrogram import __version__ as pyro_vr
import platform

__version__ = __version__


ping_msg = PING_MSG if PING_MSG else "sstart"
pic = ALIVE_PIC if ALIVE_PIC else "https://telegra.ph/file/71008a078f26dedfc62c5.jpg"
amsg = ALIVE_MSG if ALIVE_MSG else "SpamX - by AUJLA"

try:
   sah = RiZoeL.get_users(OWNER_ID)
   owner_mention = sah.mention
except:
   owner_mention = f"[{OWNER_ID}](tg://user?id={OWNER_ID})"

class Alive:
     Pic = pic
     
     msg = f"""
**⁂ {amsg} ⁂**

━───────╯•╰───────━
➠ **Master:** {owner_mention}
➠ **Python Version:** `{platform.python_version()}`
➠ **SpamX Version:** `{__version__}`
➠ **Pyrogram Version:** `{pyro_vr}`
➠ **pyRiZoeLX Version:** `{pip_vr}`
➠ **Channel:** @PunjabiChat_Group
━───────╮•╭───────━
➠ **Source Code:** [•Repo•](https://telegra.ph/file/8ffa51bb47619bb2ebb97.mp4)
     """

handler = HNDLR
Owner = int(OWNER_ID)
DATABASE_URL = DATABASE_URL
LOGS_CHANNEL = LOGS_CHANNEL

if DATABASE_URL:
   from SpamX.database import users_db
   Sudos = []
   All = users_db.get_all_sudos()
   for x in All:
     Sudos.append(x.user_id)
else:
   Sudos = sudoser
