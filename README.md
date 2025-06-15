# Orange Pi Fan Controller

Orange Pi fan controller.

## Description

This repository provides scripts that can be run on the Orange Pi that will
monitor the core temperature and start the fan when the temperature reaches
a certain threshold.

To use this code, you'll have to install a fan.

The instructions for do that you can be found on this guide for RPi: [Control Your Raspberry Pi Fan (and Temperature) with Python](https://howchoo.com/g/ote2mjkzzta/control-raspberry-pi-fan-temperature-python).

**<u>THIS SCRIPT IS SET TO CONTROL FAN WITH PIN 9 (Tested on board: Orange Pi 3 LTS)</u>**

![Orange Pi 3 LTS Pinout](/Orange-pi-3-lts-pinout.png)

## Requirements

**This script require [wiringOP](https://github.com/orangepi-xunlong/wiringOP) install on OS.**
