#!/usr/bin/python

import re,os,time,datetime,subprocess,sys
import os.path
import platform
from shutil import copyfile

import sqlite3
import time,random


class TrumpBot:

  def __init__(self):
    self.speech = list()
    self.conn = sqlite3.connect('TrumpBS.sqlite')
    self.conn.text_factory = lambda x: unicode(x, 'utf-8', 'ignore')
    self.cur = self.conn.cursor()
    self.Categories = dict()
    self.trumpspeech = list()


  def GenBS(self,topic):
    self.trumpspeech.append('%{}%'.format(topic)+"\n")
    for category,filename in self.Categories.items():
      count = random.randrange(3, 12)
      self.cur.execute('''SELECT * FROM TRUMPBS WHERE category = ? AND topic LIKE ? ORDER by RANDOM() limit ? ''',
                       (category,'%{}%'.format(topic),count))
      for row in self.cur:
        if len(row[1]) > 15:
          if "Continue reading the main story" in row[1]:
            pass
          else:
            #speech.append(category + " " + row[1])
            self.trumpspeech.append(row[1])





  def make_speech(self,topic='Default'):
    topic = topic.lower()
    f = Files()
    self.Categories['POL'] = 'politics.txt'
    self.Categories['FP'] = 'fp.txt'
    self.Categories['TRUMP'] = 'trump.txt'
    self.Categories['misc'] = 'misc.txt'
    self.Categories['RNC'] = 'rnc.txt'
    self.Categories['twitter'] = 'tweets.txt'
    self.Categories['POTUS'] = 'potus.txt'
    if 'default' in topic:
      self.cur.execute('''SELECT * FROM TRUMPBS WHERE 
                       category = ? ORDER by RANDOM() LIMIT 1''',('OPENING',))
      for row in self.cur:
        if len(row[1]) > 15:
          opening = row[1]
    self.GenBS(topic)
    tag =  self.trumpspeech[0]
    for line in self.trumpspeech[1:]:
      self.speech.append(  line.strip().encode('utf-8') )
    random.shuffle(self.speech)
    newspeech = list(self.speech[0:7])
    self.speech = list(newspeech)
    if 'default' in topic:
      self.speech[0] = opening
    newspeech = [tag] + self.speech
    #self.speech = list(newspeech)
    self.conn.close()



class DateString:

  def __init__(self):
    self.yesterday = str(datetime.date.fromtimestamp(time.time() - (60*60*24) ).strftime("%Y-%m-%d"))
    self.today = str(datetime.date.fromtimestamp(time.time()).strftime("%Y-%m-%d"))
    self.tomorrow = str(datetime.date.fromtimestamp(time.time() + (60*60*24) ).strftime("%Y-%m-%d"))
    self.now = str(time.strftime('%X %x %Z'))


class SQLTools:

  def MakeTables(self,cur):
    # Make some fresh tables using executescript()
    cur.executescript('''
  
    DROP TABLE IF EXISTS TRUMPBS;
   

    CREATE TABLE TRUMPBS (
      id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
      bullshit    BLOB,
      category    TEXT,
      topic    TEXT
    );



    ''')

class Files:

  def __init__(self):
    self.dir = ''
    self.data = []
    self.file_exists = 0

  def mkdir(self):
    if not os.path.isdir(self.dir):
      if 'Win' in platform.system():
        subprocess.call(["md", self.dir], shell=True)
      else:
        subprocess.call(["mkdir", self.dir])

  def write_file(self,filename,list):
    f = open(filename,'w')
    for line in list:
      f.write(line + '\n')
    f.close()

  def write_file_append(self,filename,list):
    f = open(filename,'a')
    for line in list:
      f.write(line)
    f.close()

  def write_log(self,logfile,logentry):
    f = open(logfile,'a')
    reportDate =  str(time.strftime("%x - %X"))
    f.write(reportDate + " :" + logentry)
    f.close()

  def read_file(self,filename):
    self.data = []
    self.file_exists = 1
    # Testing if file exists.
    if os.path.isfile(filename):
      try:
        f = open(filename,'r')
      except IOError:
        print "Failed opening ", filename
        sys.exit(2)
      for line in f:
        line = line.strip()
        self.data.append(line)
      f.close()
    else:
      # Set the file_exists flag in case caller cares.
      self.file_exists = 0

  def copy_file(self,src, dest):
    try:
      copyfile(src, dest)
    except IOError:
      print "Failed file copy ", src,dest
      sys.exit(2)

    
  def stat_file(self,fname):
    blocksize = 4096
    hash_sha = hashlib.sha256()
    f = open(fname, "rb")
    buf = f.read(blocksize)
    while 1:
      hash_sha.update(buf)
      buf = f.read(blocksize)
      if not buf:
        break    
    checksum =  hash_sha.hexdigest()
    filestat = os.stat(fname)
    filesize = filestat[6]
    return checksum,filesize



