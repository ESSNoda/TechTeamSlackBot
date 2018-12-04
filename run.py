
from slackbot.bot import Bot
from slackbot.bot import respond_to
from slackbot.bot import listen_to
from slackbot.bot import default_reply
import random
import re


DEFAULT_REPLY = "Hello, I'm tech team bot!!"
SWEET_SENTENCES = ["花火が見えない？お前がいるから大丈夫。", "恋はワインと同じ、時が経てばコクが出てくる",
                   "お前の涙は俺だけの特権", "会うのに理由っている？", "帰りたいなんて言わせないよ"]


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


@respond_to('(.*)くれ')
def stmp(message, something):
    message.reply('\stamp :{}:'.format(something))


@default_reply
def my_default_handler(message):
    message.reply(DEFAULT_REPLY)


if __name__ == "__main__":
    main()
