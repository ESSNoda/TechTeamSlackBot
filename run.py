
from slackbot.bot import Bot
from slackbot.bot import respond_to
from slackbot.bot import listen_to
from slackbot.bot import default_reply
import random
import re
import json
import requests
from datetime import timezone, timedelta
import datetime

DEFAULT_REPLY = "Hello, I'm Tech team bot!!"
SWEET_SENTENCES = ["花火が見えない？お前がいるから大丈夫。", "恋はワインと同じ、時が経てばコクが出てくる",
                   "お前の涙は俺だけの特権", "会うのに理由っている？", "帰りたいなんて言わせないよ", "お前の料理のせいで何食っても満足しねえよ", ]
WEATHER = "http://api.openweathermap.org/data/2.5/weather?units=metric&lang=ja&APPID=b71d7e713739dcd82a4fae311621eccc&id=1855078"
WEATHERF = "http://api.openweathermap.org/data/2.5/forecast?units=metric&lang=ja&APPID=b71d7e713739dcd82a4fae311621eccc&id=1855078"
JST = timezone(timedelta(hours=+9), 'JST')


def getWeather():
    result = requests.get(WEATHER)
    data = json.loads(result.text)
    return data


def getWeatherF():
    result = requests.get(WEATHERF)
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


@respond_to('天気')
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
    message.react('+1')
    isRain = False
    today = datetime.date.today().day
    weather = getWeatherF()
    message.send("今日は…")
    for item in weather['list']:
        forecastDatetime = datetime.datetime.fromtimestamp(item['dt'], JST)
        weatherDescription = item['weather'][0]['description']
        temperature = item['main']['temp']
        rainfall = 0
        message.send("{}== {}".format(forecastDatetime.day, today))
        if 'rain' in item and '3h' in item['rain']:
            rainfall = item['rain']['3h']
            if rainfall != 0 and forecastDatetime.day == today:
                isRain = True
                message.send('{0}時頃に{1}で、{2}mmぐらい降るみたい。 '.format(
                    forecastDatetime.hour, weatherDescription, rainfall))
                message.send("気温は{}℃".format(temperature))
    if isRain:
        message.send(":tired_face:")
        message.send("寒いね。暖かくして出かけよう！")
    else:
        message.send(":heart_eyes:")
        message.send("雨はふらないみたいだね！やった！")


@default_reply
def my_default_handler(message):
    message.reply(DEFAULT_REPLY)


if __name__ == "__main__":
    main()
