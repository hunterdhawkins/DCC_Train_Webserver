# DCC Train Webserver

## Introduction
This project is a Django web server that uses an open source NRMA Digital Command Control (DCC) library for the raspberry pi [https://github.com/hsanjuan/dccpi] to control and provide feedback for a DCC train.

## Overview


## Stuff to do
1. Attempt to read and write to modbus registers with pymodbus
2. Figure out what location to register the train to (intuition leads me to 3)
3. Finish creating machine vision dataset

## Setup
1. Pull repo
2. Rename train_project/local_settings.sample.py to train_project/local_settings.py
3. Fill out info in local_settings.py
4. pip install -r requirements.txt
5. Run py manage.py migrate
