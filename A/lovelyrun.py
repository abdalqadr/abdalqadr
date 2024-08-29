from telethon import events
import A.client
from A.lovely import Lovely
import time
lovely = Lovely()
client = A.client.client


@events.register(events.NewMessage)
async def lovelyrun(event):
    if '.حب' in event.raw_text:
        time.sleep(0.3)
        for d in lovely.lovely:
            time.sleep(0.3)
            await event.edit(d)