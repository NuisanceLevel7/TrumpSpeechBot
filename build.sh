#!/bin/bash

APPDIR=/home/vengle/FlaskProj/VicLab
SRCDIR=/home/vengle/projects/TrumpSpeechBot
cd $SRCDIR
${SRCDIR}/loadSpeeches.py
sleep 1
cp ${SRCDIR}/VicLab.py  $APPDIR
cp ${SRCDIR}/TrumpBS.sqlite  $APPDIR
cp ${SRCDIR}/TrumpBotModule.py  $APPDIR
cp ${SRCDIR}/templates/trumpbot.html  $APPDIR/templates
cp -R  ${SRCDIR}/static/*  $APPDIR/static
${SRCDIR}/restart.sh
