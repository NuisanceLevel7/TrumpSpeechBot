# TrumpSpeechBot
Generate random Trump speeches.

This app generates Trump speeches using a sqlite3 database of speech transcripts and a little logic. 

A load script loads the speeches and assigns category. Most of the work is done by the module and a few other
files are used to make the app work within Flask.

ToDo:

1. Update db schema to allow adding an emotion description for each entry.
2. Write a script to scan the database and add emotion categories.
3. Update the module to account for the new schema.
4. Update the app to allow the user to request specific kinds of speeches.
   like an angry speech or a whinny speech. Maybe a Hillary obsession speech and a bragging speech.
