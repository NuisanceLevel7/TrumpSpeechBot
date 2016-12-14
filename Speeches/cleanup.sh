#!/bin/bash

tar -cvf ../speeches.tar *
for file in `ls *.txt`
 do 
   iconv -f UTF8 -t US-ASCII//TRANSLIT $file >1
   mv 1 $file
 done

