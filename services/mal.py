from utils.message import CoreMessage
from jikanpy import Jikan
import re
class MyAnimeListService():
    def __init__(self):
        self.jk = Jikan()
    def search(self,m):
        m.m_type = "text"
        print("searching %s"%m.text)
        result = self.jk.search("anime",m.text,parameters={"limit": 5})
        print("finish")
        names = ["- %s\n"%x["title"] for x in result["results"]]
        m.text = "Resultados:\n"+"".join(names)
        return m
    def getAnime(self,m):
        result = self.jk.search("anime",m.text,parameters={"limit": 1})
        anime = result["results"][0]
        title = "*%s*"%anime["title"]
        episodes = "Episodes: %s"%anime["episodes"]
        airing = "🔴 Finished Airing" if not anime["airing"] else "✅ Currently Airing"
        if anime["score"]>7.5:
            score = "Score: %s 😍"%anime["score"]
        elif 5<anime["score"]<=7.5:
            score = "Score: %s 🙂"%anime["score"]
        elif 2.5<anime["score"]<=5:
            score = "Score: %s 😞"%anime["score"]
        elif anime["score"]<=2.5:
            score = "Score: %s 😠"%anime["score"]
        date = "Date: %s"%anime["start_date"][:10]
        rated = "Rated: %s"%anime["rated"]
        synopsis = "Synopsis: %s"%anime["synopsis"]
        m.text = "%s\n%s\n%s\n%s\n%s\n%s\n%s\n"%(title,episodes,airing,score,date,rated,synopsis)
        try:
            regex = re.search(r"\.jpg",anime["image_url"])
            m.img = anime["image_url"][:regex.end()]
            m.m_type = "img"
        except:
            m.m_type = "text"
        return m
