from utils.message import CoreMessage
#import os
from urllib.parse import quote
#from urllib.request import Request, urlopen
class VoiceService():
    def __init__(self,url=None):
        if not url:
            self.url = 'https://translate.google.com/translate_tts?ie=UTF-8&q=%s&tl=es-us&client=tw-ob&idx=0'
    def tts(self,m):
        m.m_type = "voice"
        m.audio = self.url%quote(m.text)
        return m
