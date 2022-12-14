# DCC Train Webserver

## Introduction
This project is a Django web server that uses an open source NRMA Digital Command Control (DCC) library for the raspberry pi [https://github.com/hsanjuan/dccpi] to control and provide feedback to and from a DCC train. Additionally this project integrates with a Automation Direct BRX PLC with the use of PyModbus [https://github.com/riptideio/pymodbus] to unload and load items on and off the DCC train. Lastly this project integrates with a camera control module built using OpenCV-Python [https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html] to determine if a material from the factory is faulty or not. 

## Overview


## Stuff to do
1. Look at what location to register the train to (intuition leads me to 3)

## Setup
1. Pull repo
2. Rename train_project/local_settings.sample.py to train_project/local_settings.py
3. Fill out info in local_settings.py
4. pip install -r requirements.txt
5. Run py manage.py migrate
