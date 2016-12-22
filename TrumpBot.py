#!/usr/bin/python
#
import sys
#
from TrumpBotModule import TrumpBot
bot = TrumpBot()
if len(sys.argv) < 2:
  bot.make_speech()
else:
  bot.make_speech(sys.argv[1])

for line in bot.speech:
    print line
