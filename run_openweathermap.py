#!/usr/bin/env python3
import time

from TrafficLight import TrafficLight
from OpenWeatherMapProvider import update_light
from OffAtNightProviderAdapter import Updater
from logger import logger

try:
    from OrangePiSetter import OrangePiSetter as Setter
except:
    from DummySetter import DummySetter as Setter

try:
    updater = Updater(update_light)
    light = TrafficLight(Setter())
    while True:
        updater(light)
        time.sleep(60*10)

except KeyboardInterrupt:
    light.stop()
    logger.debug("Goodbye.")
