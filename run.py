
from slackbot.bot import Bot
from slackbot.bot import respond_to
from slackbot.bot import listen_to
from slackbot.bot import default_reply
import random
import re
import json
import requests

DEFAULT_REPLY = "Hello, I'm Tech team bot!!"
SWEET_SENTENCES = ["花火が見えない？お前がいるから大丈夫。", "恋はワインと同じ、時が経てばコクが出てくる",
                   "お前の涙は俺だけの特権", "会うのに理由っている？", "帰りたいなんて言わせないよ"]
WEATHER = "http://api.openweathermap.org/data/2.5/weather?units=metric&APPID=b71d7e713739dcd82a4fae311621eccc&id=1855078"


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


@respond_to('天気')
def weather(message):
    message.react('yattaze')
    weather = getWeather()
    message.send("野田の天気は…")
    message.send("天気:"+weather["weather"][0]["main"]+":cloud:")
    message.send("最高気温:" + str(weather["main"]["temp_max"])+"℃:thermometer:")
    message.send("最低気温:" + str(weather["main"]["temp_min"])+"℃:thermometer:")
    message.send("現在の気温:"+str(weather["main"]["temp"])+"℃:thermometer:")


@default_reply
def my_default_handler(message):
    message.reply(DEFAULT_REPLY)


if __name__ == "__main__":
    main()
