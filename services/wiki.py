import wikipedia
from utils.message import CoreMessage

class WikiService():
    def __init__(self,lang="es"):
        wikipedia.set_lang(lang)
    def search(self,m):
        try:
            result = wikipedia.summary(m.text)
        except:
            result = wikipedia.suggest(m.text)
            if not result: result = "No hay sugerencias"
            result = "Quiza quisiste decir: "+result
        m.m_type = "text"
        m.text = result
        return m
