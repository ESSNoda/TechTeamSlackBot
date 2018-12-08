
from slackbot.bot import Bot
from slackbot.bot import respond_to
from slackbot.bot import listen_to
from slackbot.bot import default_reply
import random
import re
import json
import aiohttp
import asyncio
import async_timeout

DEFAULT_REPLY = "Hello, I'm Tech team bot!!"
SWEET_SENTENCES = ["花火が見えない？お前がいるから大丈夫。", "恋はワインと同じ、時が経てばコクが出てくる",
                   "お前の涙は俺だけの特権", "会うのに理由っている？", "帰りたいなんて言わせないよ"]
WEATHER = "http://api.openweathermap.org/data/2.5/weather?APPID=b71d7e713739dcd82a4fae311621eccc&id=1855078"


async def getWeather(session):
    async with aiohttp.ClientSession() as session:
        with async_timeout.timeout(10):
            async with session.get(WEATHER) as response:
                html = await response.text()
                data = json.loads(html)
                message.send("野田の天気は…")
                message.send(data["weather"][0]["main"])
                message.send(":yarakashi:")


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
async def weather(message):
    loop = asyncio.get_event_loop()
    loop.run_until_complete(getWeather())


@default_reply
def my_default_handler(message):
    message.reply(DEFAULT_REPLY)


if __name__ == "__main__":
    main()
