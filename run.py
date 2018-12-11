
from slackbot.bot import Bot
from slackbot.bot import respond_to
from slackbot.bot import listen_to
from slackbot.bot import default_reply
import random
import re
import json
import requests
from pytz import timezone
import datetime

DEFAULT_REPLY = "Hello, I'm Tech team bot!!"
SWEET_SENTENCES = ["花火が見えない？お前がいるから大丈夫。", "恋はワインと同じ、時が経てばコクが出てくる",
                   "お前の涙は俺だけの特権", "会うのに理由っている？", "帰りたいなんて言わせないよ", "お前の料理のせいで何食っても満足しねえよ", ]
WEATHER = "http://api.openweathermap.org/data/2.5/weather?units=metric&lang=ja&APPID=b71d7e713739dcd82a4fae311621eccc&id=1855078"


def getWeather():
    result = requests.get(WEATHER)
    data = json.loads(result.text)
    return data


def main():
    bot = Bot()
    bot.run()


@respond_to('中和')
def what(message):
    sentence = random.choice(SWEET_SENTENCES)
    message.send(sentence)
    message.react('yattaze')


@respond_to('(.*)ちょうだい')
def giveme(message, something):
    message.reply('はい、 {}だよ。'.format(something))


@respond_to('今の天気')
def weather(message):
    message.react('+1')
    weather = getWeather()
    message.send("野田の今の天気は…")
    message.send("天気:" + weather["weather"][0]["main"])
    message.send("詳細:"+weather["weather"][0]["description"])
    message.send("最高気温:" + str(weather["main"]["temp_max"])+"℃ :thermometer:")
    message.send("最低気温:" + str(weather["main"]["temp_min"])+"℃ :thermometer:")
    message.send("現在の気温:" + str(weather["main"]["temp"]) + "℃ :thermometer:")


@respond_to('雨')
def rainweather(message):
    isRain = False
    message.react('+1')
    weather = getWeather()
    message.send("今日は…")
    for item in weather['list']:
        forecastDatetime = timezone(
            'Asia/Tokyo').localize(datetime.datetime.fromtimestamp(item['dt']))
        weatherDescription = item['weather'][0]['description']
        temperature = item['main']['temp']
        rainfall = 0
        if 'rain' in item and '3h' in item['rain']:
            rainfall = item['rain']['3h']
            isRain = True
            if rainfall != 0:
                message.send('日時:{0} 天気:{1} 気温(℃):{2} 雨量(mm):{3}'.format(
                    forecastDatetime, weatherDescription, temperature, rainfall))
    if isRain:
        message.send("雨が降るみたい！")
    else:
        message.send("ふらないよ！:+1:")


@default_reply
def my_default_handler(message):
    message.reply(DEFAULT_REPLY)


if __name__ == "__main__":
    main()
