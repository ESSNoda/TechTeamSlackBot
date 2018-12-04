
from slackbot.bot import Bot
from slackbot.bot import respond_to
from slackbot.bot import listen_to
import re


def main():
    bot = Bot()
    bot.run()


@respondo_to('中和')
def what(message):
    message.reply('花火が見えない？お前がいるから大丈夫。')
    message.react('+1')


@respond_to('(.*) ちょうだい')
def giveme(message, something):
    message.reply('はい、 {}だよ。'.format(something))


if __name__ == "__main__":
    main()
