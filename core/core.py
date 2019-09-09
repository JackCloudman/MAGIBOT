from channels.messenger import Messenger
import threading
from services import wiki,mal,voice,weather, spam_message
from services.translate import YandexTranslate as YT
import re
class Core():
    ch = []
    ws = wiki.WikiService()
    mals = mal.MyAnimeListService()
    tts = voice.VoiceService()
    wx = weather.WeatherService()
    t = YT()
    spam = spam_message.SpamService()

    commands = {"wiki":ws.search,
                "asearch":mals.search,
                "anime":mals.getAnime,
                "tts":tts.tts,
                "wx":wx.weatherByplace,
                "t": t.translate,
                "t_from":t.translate_from,
                "is_spam":spam.is_spam,
                }
    def __init__(self,prefix="!"):
        print("Starting core...")
        self.ch.append(Messenger(prefix=prefix))
    def start(self):
        threads = []
        print("init channel")
        for c in self.ch:
            threads.append(threading.Thread(target=c.sniffer))
        for t in threads:
            t.start()
        print("Success! Listening...")
        # Process queue for each channel
        while True:
            for c in self.ch:
                if c.queue:
                    result = self.execute(c.queue[0])
                    if result:
                        try:
                            c.sendM(result)
                        except Exception as e:
                            print(e)
                    c.queue.pop(0)

    def execute(self,m):
        m.text = m.text[1:]
        try:
            regex = re.search(r"\w+",m.text)
            command = regex.group()
            m.text = m.text[regex.end()+1:]
            if not m.text:
                return None
        except Exception as e:
            print(e)
            return None
        if command in self.commands:
            return self.commands[command](m)
        else:
            return None
