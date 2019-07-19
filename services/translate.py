from yandex.Translater import Translater
import re
class YandexTranslate():
    def __init__(self,to_lang='es',from_lang='en'):
        token = "TOKEN" #get here https://translate.yandex.com/developers/keys
        tr = Translater()
        tr.set_key(token)
        tr.set_to_lang(to_lang)
        tr.set_from_lang(from_lang)
        self.from_lang_default = from_lang
        self.tr = tr
    def translate(self,m):
        m.m_type = "text"
        self.tr.set_text(m.text)
        m.text = self.tr.translate()
        return m
    def translate_from(self,m):
        regex = re.search("\w+",m.text)
        try:
            lang = regex.group()
            self.tr.set_from_lang(lang)
            m.text = m.text[regex.end()+1:]
            m = self.translate(m)
        except:
            m.text = "No he podido hacer la traduccion"
            m.m_type = "text"
        self.tr.set_from_lang(self.from_lang_default)
        return m
