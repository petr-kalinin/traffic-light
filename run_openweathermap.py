#!/usr/bin/env python3
import time

#from DummySetter import DummySetter
from OrangePiSetter import OrangePiSetter
from TrafficLight import TrafficLight
from OpenWeatherMapProvider import update_light
from OffAtNightProviderAdapter import Updater

try:
    updater = Updater(update_light)
    light = TrafficLight(OrangePiSetter())
    while True:
        updater(light)
        time.sleep(60*10)

except KeyboardInterrupt:
    light.stop()
    print ("Goodbye.")
