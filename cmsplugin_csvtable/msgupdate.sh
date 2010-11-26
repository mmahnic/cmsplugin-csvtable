#!/bin/bash

if [ ! -d locale ]; then
   mkdir locale
fi
if [ ! -d locale/sl ]; then
   django-admin makemessages -l sl -e html,htmi -e py
fi

#if [ ! -d locale/en ]; then
#   django-admin makemessages -l en -e html,htmi -e py
#fi

django-admin makemessages -a -e html,htmi -e py
django-admin compilemessages
