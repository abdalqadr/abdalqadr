from telethon import events
import A.client
client = A.client
import random

gn = ["""
┌▀█┌▀█┌▀█┌▀█┌▀█┌▀█┌▀█
┌▀█╔══╗╔══╗╔══╗╔══╗▀█
┌▀█║╔═╣║╔╗║║╔╗║╚╗╗║▀█
┌▀█║╚╗║║╚╝║║╚╝║╔╩╝║▀█
┌▀█╚══╝╚══╝╚══╝╚══╝▀█
┌▀█┌▀█┌▀█┌▀█┌▀█┌▀█┌▀█
┌▀█░░░░░░░░░░░░░░░░▀█
┌▀█░░█▌▌█▐▀▐░▌▀█▀░░▀█
┌▀█░░█▐▌█▐▐▐▀▌░█░░░▀█
┌▀█░░█░▌█▐█▐░▌░█░░░▀█
┌▀█░░░░░░░░░░░░░░░░▀█
┌▀█┌▀█┌▀█┌▀█┌▀█┌▀█┌▀█ 
""",
"""
🌙.     *       ☄️      
🌟   .  *       .         
                       *   .      🛰     .        ✨      *
  .     *   SLEEP WELL        🚀     
      .              . . SWEET DREAMS 🌙
. *       🌏 GOOD NIGHT         *
                     🌙.     *       ☄️      
🌟   .  *       .         
                       *   .      🛰     .        ✨      *
"""]

@events.register(events.NewMessage(pattern=".نام"))
async def goodnight(event):
  ggn = random.choice(gn)
  return await event.edit(ggn)