#!/usr/bin/python
#
#
import sqlite3
import re
import time
from TrumpBotModule import Files
from TrumpBotModule import SQLTools

conn = sqlite3.connect('TrumpBS.sqlite')
conn.text_factory = lambda x: unicode(x, 'utf-8', 'ignore')
cur = conn.cursor()

db = SQLTools()
db.MakeTables(cur)

f = Files()

Categories = dict()
Categories['POL'] = 'politics.txt'
Categories['OPENING'] = 'openings.txt'
Categories['FP'] = 'fp.txt'
Categories['TRUMP'] = 'trump.txt'
Categories['misc'] = 'misc.txt'
Categories['twitter'] = 'tweets.txt'
Categories['RNC'] = 'rnc.txt'

# -*- coding: utf-8 -*-
def strip_non_ascii(string):
    ''' Returns the string without non ASCII characters'''
    stripped = (c for c in string if 0 < ord(c) < 127)
    return ''.join(stripped)


def loadBS():
  topics = dict()

  topics['media'] = [' pundit',' cnn',' media','new york times', ' ny ','the press ']
  topics['ocd'] = ['hillary','obama','bush']
  topics['twitter'] = ['twitter']
  topics['bragging'] = [' i am a ',' me ',' love donald ',
         "nobody.*trump", 'I own ',' i was the one ']
  for category,filename in Categories.items():
    f.read_file('Speeches/' + filename)
    for line in f.data:
      topic = 'default '
      if category == 'twitter':
        topic = 'default ' +  'twitter '
      topic_keys = topics.keys()
      foundkeys = dict()
      for thiskey in topic_keys:
        for keyword in topics[thiskey] :
          low = line.lower()
          #if low.find(keyword) >= 0 :
          if re.search(keyword,low):
            foundkeys[thiskey] = 1;
      for matches in foundkeys.keys():
        topic = topic + matches + ' '    
      #line = strip_non_ascii(line)
      if len(line) > 3:
        cur.execute('''INSERT OR IGNORE INTO TRUMPBS (bullshit, category, topic)
          VALUES ( ?,?,? )''', ( line, category, topic ) )

  conn.commit()




# SELECT * FROM TRUMPBS WHERE category = 'FP' ORDER BY RANDOM() LIMIT 4;
loadBS()
conn.commit()
conn.close()
