"""Check if userbot alive. If you change these, you become the gayest gay such that even the gay world will disown you."""
import asyncio
from telethon import events
from uniborg.util import admin_cmd, sudo_cmd, edit_or_reply
from userbot import ALIVE_NAME
from telethon.tl.types import ChannelParticipantsAdmins
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Unknown"
PM_IMG = "https://telegra.ph/file/b7a072627232640a7bf2a.png"
pm_caption = "`PSY IS:` **RUNNING**\n\n"
pm_caption += "**SYSTEM STATUS**\n"
pm_caption += "`TELETHON VERSION:` **1.15.0**\n`Python:` **3.7.4**\n"
pm_caption += "`DATABASE STATUS:` **SUCCESS**\n"
pm_caption += "**Current Branch** : `master`\n"
pm_caption += "**PSY VERSION** : `1.0`\n"
pm_caption += f"**My Boss** : {DEFAULTUSER} \n"
pm_caption += "**Heroku Database** : `VPS - Working Running`\n\n"
pm_caption += "Copyright : By [PSY USERBOT] {A private repo by @PSY_CRACKER}"


@borg.on(admin_cmd(pattern=r"alive"))
@borg.on(sudo_cmd(pattern=r"alive", allow_sudo=True))
async def (alive):
    chat = await alive.get_chat()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG,caption=pm_caption)
    await alive.delete()
