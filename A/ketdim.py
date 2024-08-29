from telethon import events
import time
import A.client
client = A.client.client


ketdi = ["░░░░░░🚜░░░░░░🏠\n█████████████████",
 "░░░░░░🚜░░░░░🚶🏠\n█████████████████",
 "░░░░░░🚜░░░░🚶░🏠 \n█████████████████",
 "░░░░░░🚜░░🚶░░░🏠 \n█████████████████",
 "░░░░░░🚜🚶░░░░░🏠 \n█████████████████",
 "░░░░░░🚜░░░░🇰░🏠 \n█████████████████",
 "░░░░░🚜░░░░░░░░🏠 \n█████████████████",
 "░░░░🚜░░░🇰 🇪 ░🏠\n█████████████████",
 "░░░🚜░🇰 🇪 🇹░░🏠\n█████████████████",
 "░🚜░🇰 🇪 🇹 🇩 🏠\n█████████████████",
 "🚜░🇰 🇪 🇹 🇩 🇮🏠\n █████████████████",
 "🇰 🇪 🇹 🇩 🇮 🇲🏠\n█████████████████"]
@events.register(events.NewMessage)
async def ketdihandlers(event):
		if '.ذهبت' in event.raw_text:
			time.sleep(0.3)
			for d in ketdi:
				time.sleep(0.3)
				await event.edit(d)