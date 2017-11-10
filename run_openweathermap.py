#!/usr/bin/env python3
import time

from OrangePiSetter import OrangePiSetter
from TrafficLight import TrafficLight
from OpenWeatherMapProvider import update_light

try:
    light = TrafficLight(OrangePiSetter())
    while True:
        update_light(light)
        time.sleep(60*10)

except KeyboardInterrupt:
    light.stop()
    print ("Goodbye.")
