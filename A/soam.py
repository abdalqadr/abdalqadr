async def final_send_w3d_baksheesh(event):
import base64
import asyncio
from telethon import events
from asyncio import sleep
from telethon.sync import TelegramClient
from telethon import events
from telethon.events import NewMessage
from phoenix import client
import re


finalll = client.client 

final = False
async def final_nshr(finalll, sleeptimet, chat, message, seconds):
    global final
    final = True
    while final:
        if message.media:
            sent_message = await finalll.send_file(chat, message.media, caption=message.text)
        else:
            sent_message = await finalll.send_message(chat, message.text)
        await asyncio.sleep(sleeptimet)

async def final_allnshr(finalll, sleeptimet, message):
    global final
    final = True
    final_chats = await finalll.get_dialogs()
    while final:
        for chat in final_chats:
            if chat.is_group:
                try:
                    if message.media:
                        await finalll.send_file(chat.id, message.media, caption=message.text)
                    else:
                        await finalll.send_message(chat.id, message.text)
                except Exception as e:
                    print(f"Error in sending message to chat {chat.id}: {e}")
        await asyncio.sleep(sleeptimet)

super_groups = ["super", "سوبر"]
async def final_supernshr(finalll, sleeptimet, message):
    global final
    final = True
    final_chats = await finalll.get_dialogs()
    while final:
        for chat in final_chats:
            chat_title_lower = chat.title.lower()
            if chat.is_group and any(keyword in chat_title_lower for keyword in super_groups):
                try:
                    if message.media:
                        await finalll.send_file(chat.id, message.media, caption=message.text)
                    else:
                        await finalll.send_message(chat.id, message.text)
                except Exception as e:
                    print(f"Error in sending message to chat {chat.id}: {e}")
        await asyncio.sleep(sleeptimet)
@finalll.on(events.NewMessage(outgoing=True, pattern=r"^\.نشر (\d+) (@?\S+)$"))
async def final_handler(event):
    if not isinstance(event, events.NewMessage.Event):
        return

    await event.delete()
    parameters = re.split(r'\s+', event.text.strip(), maxsplit=2)
    if len(parameters) != 3:
        return await event.reply("☠️ يجب استخدام كتابة صحيحة الرجاء التاكد من الامر اولا ☠️")
    seconds = int(parameters[1])
    chat_usernames = parameters[2].split()
    finalll = event.client
    global final
    final = True
    message = await event.get_reply_message()
    for chat_username in chat_usernames:
        try:
            chat = await finalll.get_entity(chat_username)
        except Exception as e:
            print(f"Error in sending message to chat {chat.id}: {e}")

@finalll.on(events.NewMessage(outgoing=True, pattern=r"^\.نقط (\d+)$"))
async def dot_handler(event):
    if not isinstance(event, events.NewMessage.Event):
        return

    await event.delete()
    seconds = int(event.pattern_match.group(1))
    reply_to_msg = await event.get_reply_message()
    if not reply_to_msg:
        return await event.reply("☠️ يجب الرد على رسالة لاستخدام هذا الأمر.")

    global final
    final = True

    while final:
        await reply_to_msg.reply(".")
        await asyncio.sleep(seconds)

@finalll.on(events.NewMessage(outgoing=True, pattern=r"^\.مكرر (\d+)$"))
async def repeat_handler(event):
    if not isinstance(event, events.NewMessage.Event):
        return

    await event.delete()
    seconds = int(event.pattern_match.group(1))
    message = await event.get_reply_message()
    if not message:
        return await event.reply("☠️ يجب الرد على رسالة لاستخدام هذا الأمر.")

    global final
    final = True

    while final:
        await message.respond(message)
        await asyncio.sleep(seconds)

# ===== جزء .راتب وعد =====

@finalll.on(events.NewMessage(outgoing=True, pattern=r"^\.راتب وعد(?:\s|$)([\s\S]*)"))
async def final_w3d_salary(event):
    if not isinstance(event, events.NewMessage.Event):
        return

    global its_w3d_salary  
    
    await event.delete()
    if not its_w3d_salary:
        its_w3d_salary = True
        if event.is_group:
            await final_send_w3d_salary(event)
        else:
            await event.edit("**هذا الأمر يمكن استخدامه فقط في المجموعات!**")

async def final_send_w3d_salary(event):
    await event.respond('راتب')
    await asyncio.sleep(660)
    global its_w3d_salary 
    if its_w3d_salary:
        await final_send_w3d_salary(event)  

@finalll.on(events.NewMessage(outgoing=True, pattern=r"^\.ايقاف راتب وعد(?:\s|$)([\s\S]*)"))
async def final_stop_w3d_salary(event):
    if not isinstance(event, events.NewMessage.Event):
        return

    global its_w3d_salary
    its_w3d_salary = False
    await event.edit("**تم تعطيل راتب وعد بنجاح ✅**")

# ===== جزء .بخشيش وعد =====

@finalll.on(events.NewMessage(outgoing=True, pattern=r"^\.بخشيش وعد(?:\s|$)([\s\S]*)"))
async def final_w3d_baksheesh(event):
    if not isinstance(event, events.NewMessage.Event):
        return

    global its_w3d_baksheesh  

    await event.delete()
    if not its_w3d_baksheesh:
        its_w3d_baksheesh = True
        if event.is_group:
            await final_send_w3d_baksheesh(event)
        else:
            await event.edit("**هذا الأمر يمكن استخدامه فقط في المجموعات!**")

async def final_send_w3d_baksheesh(event):
    await event.respond('بخشيش')
    await asyncio.sleep(660)
    global its_w3d_baksheesh
    if its_w3d_baksheesh:
        await final_send_w3d_baksheesh(event)  

@finalll.on(events.NewMessage(outgoing=True, pattern=r"^\.ايقاف بخشيش وعد(?:\s|$)([\s\S]*)"))
async def final_stop_w3d_baksheesh(event):
    if not isinstance(event, events.NewMessage.Event):
        return

    global its_w3d_baksheesh
    its_w3d_baksheesh = False
    await event.edit("**᯽︙ تم تعطيل بخشيش وعد بنجاح ✓ **")
# ===== جزء .سرقة وعد =====
@finalll.on(events.NewMessage(outgoing=True, pattern=r"^\.سرقة وعد(?:\s|$)([\s\S]*)"))
async def final_w3d_serqa(event):
    if not isinstance(event, events.NewMessage.Event):
        return

    global its_w3d_serqa  

    await event.delete()
    if not its_w3d_serqa:
        its_w3d_serqa = True
        if event.is_group:
            message = event.pattern_match.group(1).strip()
            if message:
                await final_send_w3d_serqa_message(event, message)  
            else:
                await event.edit("**يرجى كتابة ايدي الشخص مع الامر!**")

async def final_send_w3d_serqa_message(event, message): 
    await event.respond(f"زرف {message}")
    await asyncio.sleep(660)
    global its_w3d_serqa
    if its_w3d_serqa:
        await final_send_w3d_serqa_message(event, message)

@finalll.on(events.NewMessage(outgoing=True, pattern=r"^\.ايقاف سرقة وعد(?:\s|$)([\s\S]*)"))
async def final_stop_w3d_serqa(event):
    if not isinstance(event, events.NewMessage.Event):
        return

    global its_w3d_serqa
    its_w3d_serqa = False
    await event.edit("** ᯽︙ تم ايقاف السرقة بنجاح ✓ **")