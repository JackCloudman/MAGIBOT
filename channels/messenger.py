from utils.channel import Channel
from utils.message import CoreMessage
from fbchat import Client
from fbchat.models import *
import json
from getpass import  getpass
class Messenger(Channel,Client):
    def __init__(self,prefix):
        self.Clogin()
        self.prefix = prefix
    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
        text = message_object.text
        if text and text[0]==self.prefix:
            m = CoreMessage(m_type="message")
            m.text = text
            m.thread_id=thread_id
            m.thread_type=thread_type
            self.queue.append(m)
    def Clogin(self):
        try:
            with open('messenger.json','r') as f:
                cookie = json.load(f)
            Client.__init__(self,"","",user_agent=None,session_cookies=cookie)
        except:
            while True:
                email = input("Email: ")
                password = getpass()
                cookie = None
                try:
                    Client.__init__(self,email,password)
                    break
                except Exception as e:
                    print(e)
                    print("Login error")
        if not cookie:
            self.storeCredentials(self.getSession()) if input("Store credentials y/n? ") == "y" else None
    def storeCredentials(self,cookie):
        with open('messenger.json','w') as f:
            json.dump(cookie,f)
    def sniffer(self):
        self.listen()
    def sendM(self,m):
        if m.m_type == "text":
            m_object = Message(text=m.text)
            self.send(m_object, thread_id=m.thread_id, thread_type=m.thread_type)
        elif m.m_type == "img":
            m_object = Message(text=m.text)
            self.sendRemoteImage(m.img,message=m_object,thread_id=m.thread_id, thread_type=m.thread_type)
        elif m.m_type == "voice":
            self.sendRemoteVoiceClips(m.audio,thread_id=m.thread_id, thread_type=m.thread_type)
