import requests
import json
import sys
print('inicio')
class WeatherService():
    def __init__(self, base_url=None, api_token=None):
        self.base_url = 'https://api.openweathermap.org/data/2.5/weather?q=London,uk&APPID='
        self. api_token = 'c366b0cc0ec061765d5483ebb6d10ba6'

    def weathertest(self):
        r = requests.get(url=self.base_url+self.api_token)
        return r.json()

    def weatherByplace(self,m= 'Mexico city'):
        base_by_place = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid='.format(m.text)
        try:
            r = requests.get(url=base_by_place+self.api_token)
            data= json.loads(r.content)
            m.m_type='text'
            temp_text ='Weather: '+str(data['main']['temp'])+' °C 📈'
            min_max ='Temperature from {} to {}'.format(str(data['main']['temp_min']), str(data['main']['temp_max']))
            wind='wind: {} m/s💨'.format(data['wind']['speed'])
            m.text = "%s\n%s\n%s"%(temp_text, min_max, wind)
        except:
            m.m_type = 'text'
            m.text=""
        return m
