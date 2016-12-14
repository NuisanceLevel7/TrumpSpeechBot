#!/usr/bin/python
#
#
from TrumpBotModule import TrumpBot

bot = TrumpBot()
bot.make_speech()

for line in bot.speech:
    print line
