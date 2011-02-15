#!/bin/bash - 

target="csvtable.css"
while true; do
   for fin in *.scss; do
      if [ $fin -nt $target ]; then
         sass --no-cache csvtable.scss $target
         echo "$(date): $target updated."
         break
      fi
   done
   sleep 1
done
