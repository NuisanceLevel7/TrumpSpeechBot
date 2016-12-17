#!/bin/bash

APPDIR=/home/vengle/FlaskProj/VicLab
./loadSpeeches.py
sleep 1
cp ./VicLab.py  $APPDIR
cp ./TrumpBS.sqlite  $APPDIR
cp ./TrumpBotModule.py  $APPDIR
./restart.sh
