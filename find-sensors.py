#!/usr/bin/env python3

from ruuvitag_sensor.ruuvi import RuuviTagSensor
import ruuvitag_sensor.log

ruuvitag_sensor.log.enable_console()

RuuviTagSensor.find_ruuvitags()
