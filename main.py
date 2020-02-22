import time

import kivy
import requests
import datetime
import json
from kivy.app import App
from kivy.clock import Clock
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
import spotipy

SPOTIPY_CLIENT_ID="41ab06391a18471bad7528fa4952ed8d"
SPOTIPY_CLIENT_SECRET="eff525cb68ee46c8a3623eb627ff00f5"

apikey = "c3c492a15455fbdbf933ae22da3863f7"
city = "kalamazoo"

def getWeather():
    r = requests.get("http://api.openweathermap.org/data/2.5/forecast?id=524901&APPID=c3c492a15455fbdbf933ae22da3863f7")
    data = r.json()
    temp = data["list"][0]["main"]["temp"]
    weather = data["list"][0]["weather"][0]["main"]
    return temp, weather

class Home(App):

    def build(self):
        temp, weather = getWeather()
        temp = round((temp - 273) * 9/5 + 32)
        layout = FloatLayout(size=(300, 300))
        date = datetime.datetime.now()
        timeString = date.strftime("%I:%M %p")
        dateString = date.strftime("%B %d, %Y")
        tempString = "It is currently " + str(temp) + " degrees"
        self.temperature = Label(text=tempString, size_hint=(.6, .6), pos=(150, 900), font_size=30)
        self.temperature.size_hint = (0.1, 0.1)
        self.time = Label(text=timeString, size_hint=(.6, .6), pos=(1700, 900), font_size=30)
        self.time.size_hint = (0.1, 0.1)
        self.day = Label(text=dateString, size_hint=(.6, .6), pos=(1650, 850), font_size=30)
        self.day.size_hint = (0.1, 0.1)
        layout.add_widget(self.day)
        layout.add_widget(self.time)
        layout.add_widget(self.temperature)
        t = 5.0   # 1/60th of a second, use 1.0 instead to update every second
        Clock.schedule_interval(self.update, t)
        return layout

    def update(self, dt):
        temp, weather = getWeather()
        temp = round((temp - 273) * 9 / 5 + 32)
        date = datetime.datetime.now()
        timeString = date.strftime("%I:%M %p")
        dateString = date.strftime("%B %d, %Y")
        self.temperature.text = "It is currently " + str(temp) + " degrees"
        self.time.text = timeString
        self.day.text = dateString

if __name__ == "__main__":
    Home().run()