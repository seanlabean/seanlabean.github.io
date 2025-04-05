#!/bin/bash
SITE=./site
INC=./inc

echo -e "Clearing $SITE contents..."
rm $SITE/*

echo -e "Building from main.py - sending to $SITE"
python3 main.py
cp external/* site/