#!/usr/bin/python
#
#
import sqlite3
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
Categories['RNC'] = 'rnc.txt'

# -*- coding: utf-8 -*-
def strip_non_ascii(string):
    ''' Returns the string without non ASCII characters'''
    stripped = (c for c in string if 0 < ord(c) < 127)
    return ''.join(stripped)


def loadBS():
 
  for category,filename in Categories.items():
    f.read_file('Speeches/' + filename)
    for line in f.data:
      #line = strip_non_ascii(line)
      if len(line) > 3:
        #cur.execute('''INSERT OR IGNORE INTO TRUMPBS (bullshit, category)
        #  VALUES ( ?,? )''', ( line.encode('utf-8'), category ) )
        cur.execute('''INSERT OR IGNORE INTO TRUMPBS (bullshit, category)
          VALUES ( ?,? )''', ( line, category ) )

  conn.commit()




# SELECT * FROM TRUMPBS WHERE category = 'FP' ORDER BY RANDOM() LIMIT 4;
loadBS()
conn.commit()
conn.close()
