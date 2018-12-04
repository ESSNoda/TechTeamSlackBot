
from slackbot.bot import Bot
from slackbot.bot import respond_to
from slackbot.bot import listen_to
from slackbot.bot import default_reply
import re


DEFAULT_REPLY = "Hello, I'm tech team bot!!"


def main():
    bot = Bot()
    bot.run()


@respond_to('中和')
def what(message):
    message.send('花火が見えない？お前がいるから大丈夫。')
    message.react('+1')


@respond_to('(.*)ちょうだい')
def giveme(message, something):
    message.reply('はい、 {}だよ。'.format(something))


@default_reply
def my_default_handler(message):
    message.reply(DEFAULT_REPLY)


if __name__ == "__main__":
    main()
