from telethon import events
import A.client
from A.magic import Magic
import time
magic = Magic()
client = A.client.client
@events.register(events.NewMessage)
async def magicrun(event):
		if '.سحر' in event.raw_text:
			time.sleep(0.3)
			for d in magic.magic:
				time.sleep(0.3)
				await event.edit(d)