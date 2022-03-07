#!/bin/bash
iconv -f cp1250 -t utf-8 "$1" | tr -d '\r' | python3 process.py | csvcut -d ";" -c "#Data operacji,#Kwota,#Opis operacji"
