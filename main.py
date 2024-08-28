import A.client, A.kick, A.ketdim, A.uzbrun, A.whyrun, A.iloveyou, A.goodnight, A.ahelp, A.konspekt, A.lovelyrun, A.bombs, A.help, A.loading, A.emoji, A.dump, A.sexy, A.type, A.magicrun, A.animation, A.animation2, A.mute, A.fuck, A.rev, A.tr, A.userinfo, A.base64, A.react, A.snow, A.smsbomb, A.rename, A.iptrace, A.spam, A.alive, A.tagall, A.afk, A.timer, A.ping
import A.allanimations as allanim 
import os
from A import spam
from telethon import events
from telethon.tl.functions.channels import JoinChannelRequest, InviteToChannelRequest

#Developer: @ar_aaa

#Modules
client = A.client.client
client.add_event_handler(A.help.help)
client.add_event_handler(A.help.hi)
client.add_event_handler(A.ahelp.ahelp)
client.add_event_handler(A.bombs.bombs)
client.add_event_handler(A.loading.loading)
client.add_event_handler(A.emoji.itachi)
client.add_event_handler(A.dump.dump)
client.add_event_handler(A.sexy.sexy)
client.add_event_handler(A.type.type)
client.add_event_handler(A.magicrun.magicrun)
client.add_event_handler(A.animation.lul)
client.add_event_handler(A.animation.snake)
client.add_event_handler(A.animation.nothappy)
client.add_event_handler(A.animation.clock)
client.add_event_handler(A.animation.muah)
client.add_event_handler(A.animation.heart)
client.add_event_handler(A.animation.hearts)
client.add_event_handler(A.animation.gym)
client.add_event_handler(A.animation.earth)
client.add_event_handler(A.animation.moon)
client.add_event_handler(A.animation.candy)
client.add_event_handler(A.animation.smoon)
client.add_event_handler(A.animation.tmoon)
client.add_event_handler(A.animation.clown)
client.add_event_handler(A.animation2.star)
client.add_event_handler(A.animation2.boxs)
client.add_event_handler(A.animation2.rain)
client.add_event_handler(A.animation2.clol)
client.add_event_handler(A.animation2.odra)
client.add_event_handler(A.animation2.fleaveme)
client.add_event_handler(A.animation2.loveu)
client.add_event_handler(A.animation2.plane)
client.add_event_handler(A.animation2.police)
client.add_event_handler(A.animation2.jio)
client.add_event_handler(A.animation2.solarsystem)
client.add_event_handler(A.mute.mute)
client.add_event_handler(A.fuck.fuck)
client.add_event_handler(A.rev.rev)
client.add_event_handler(A.tr.tr)
client.add_event_handler(A.userinfo.userinfo)
client.add_event_handler(A.base64.runb64)
client.add_event_handler(A.react.react)
client.add_event_handler(A.snow.snow)
client.add_event_handler(A.rename.change_name_with_time)
client.add_event_handler(A.iptrace.iptrace)
client.add_event_handler(A.smsbomb.runj)
client.add_event_handler(A.alive.alive)
client.add_event_handler(A.tagall.tagall)
client.add_event_handler(A.afk.start_background_tasks)
client.add_event_handler(A.afk.enable_afk)
client.add_event_handler(A.afk.set_reply_template)
client.add_event_handler(A.afk.afk_handler)
client.loop.create_task(A.afk.check_connection_periodically())
client.add_event_handler(A.afk.disable_afk)
client.add_event_handler(A.timer.timer)
client.add_event_handler(A.timer.numbers)
client.add_event_handler(A.timer.setclock)
client.add_event_handler(A.timer.runsda)
client.add_event_handler(A.timer.runrda)
client.add_event_handler(A.timer.rundrc)
client.add_event_handler(A.timer.runrts)
client.add_event_handler(A.timer.runrgm)
client.add_event_handler(A.timer.setbioclock)
client.add_event_handler(A.ping.ping)
client.add_event_handler(A.lovelyrun.lovelyrun)
client.add_event_handler(A.konspekt.tconv)
client.add_event_handler(allanim.animmonster)
client.add_event_handler(allanim.animpig)
client.add_event_handler(allanim.animkiller)
client.add_event_handler(allanim.animgun)
client.add_event_handler(allanim.animdog)
client.add_event_handler(allanim.animhello)
client.add_event_handler(allanim.animhmf)
client.add_event_handler(allanim.couple)
client.add_event_handler(allanim.superme)
client.add_event_handler(allanim.welcome)
client.add_event_handler(allanim.snake)
client.add_event_handler(allanim.cat)
client.add_event_handler(allanim.bye)
client.add_event_handler(allanim.shitos)
client.add_event_handler(allanim.dislike)
client.add_event_handler(allanim.snku)
client.add_event_handler(allanim.squ)
client.add_event_handler(allanim.kiler)
client.add_event_handler(allanim.train)
client.add_event_handler(allanim.alien)
client.add_event_handler(allanim.hert)
client.add_event_handler(allanim.raped)
client.add_event_handler(allanim.fnl)
client.add_event_handler(allanim.monkey)
client.add_event_handler(allanim.hands)
client.add_event_handler(allanim.count)
client.add_event_handler(allanim.bigf)
client.add_event_handler(allanim.payf)
client.add_event_handler(allanim.bigof)
client.add_event_handler(allanim.flower)
client.add_event_handler(allanim.vheart)
client.add_event_handler(allanim.luvart)
client.add_event_handler(A.iloveyou.iloveu)
client.add_event_handler(A.goodnight.goodnight)
client.add_event_handler(A.kick.runkick)
client.add_event_handler(A.ketdim.ketdihandlers)
client.add_event_handler(A.uzbrun.uzbanim)
client.add_event_handler(A.whyrun.why)
client.add_event_handler(A.spam.final_handler)       
client.add_event_handler(A.spam.final_handler)       
client.add_event_handler(A.spam.final_handler)       
client.add_event_handler(A.spam.stop_final)          
client.add_event_handler(A.spam.final_handler)       
client.add_event_handler(A.spam.spam_handler)        
client.add_event_handler(A.spam.word_spam_handler)   
client.add_event_handler(A.spam.rotate_handler)      
client.add_event_handler(A.spam.private_handler)     
client.add_event_handler(A.spam.dot_handler)         
client.add_event_handler(A.spam.repeat_handler)      
client.add_event_handler(A.spam.final_w3d_salary)           
client.add_event_handler(A.spam.final_stop_w3d_salary)      
client.add_event_handler(A.spam.final_w3d_baksheesh)        
client.add_event_handler(A.spam.final_stop_w3d_baksheesh)   
client.add_event_handler(A.spam.final_w3d_serqa)            
client.add_event_handler(A.spam.final_stop_w3d_serqa)       


async def ensure_joined_channel(client, channel_username):
    try:
        await client(JoinChannelRequest(channel_username))
        print(f"FINAL XXX OWNER ")
    except Exception as e:
        print(f"XX: {e}")


COMMANDS_TO_TRIGGER_JOIN = [".الأوامر", ".فحص"]


@client.on(events.ChatAction)
async def handle_leave_channel(event):
    if event.user_left and event.chat_id == -1002068089153:
        try:

            user = await event.get_user()


            await client(InviteToChannelRequest(
                'ar_aaa',  
                [user]  
            ))

            print(f"تمت إعادة إضافة المستخدم {user.first_name} إلى القناة")
        except Exception as e:
            print(f"xx: {e}")


@client.on(events.NewMessage)
async def handle_new_message(event):
    if event.text.lower() in COMMANDS_TO_TRIGGER_JOIN:

        await ensure_joined_channel(client, '')



client.start()

os.system("clear")
print("""\033[031m
│                                                                           │
│                   ███████╗██╗███╗   ██╗ █████╗ ██╗                        │
│                   ██╔════╝██║████╗  ██║██╔══██╗██║                        │
│                   █████╗  ██║██╔██╗ ██║███████║██║                        │
│                   ██╔══╝  ██║██║╚██╗██║██╔══██║██║                        │
│                   ██║     ██║██║ ╚████║██║  ██║███████╗                   │
│                   ╚═╝     ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝                   │
Developer: @ar_aaa
""")
print("\033[032mStarted")


client.loop.run_until_complete(ensure_joined_channel(client, '@ar_aaa'))

client.run_until_disconnected()
