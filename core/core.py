from channels.messenger import Messenger
import threading
from services import wiki
import re
class Core():
    ch = []
    ws = wiki.WikiService()
    commands = {"wiki":ws.search}
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
                        c.sendM(result)
                    c.queue.pop(0)

    def execute(self,m):
        m.text = m.text[1:]
        try:
            regex = re.search(r"\w+",m.text)
            command = regex.group()
            m.text = m.text[regex.end()+1:]
        except Exception as e:
            print(e)
            return None
        if command in self.commands:
            return self.commands[command](m)
        else:
            return None
