#!/usr/bin/env python3
import time

from DummySetter import DummySetter
from TrafficLight import TrafficLight
from YandexJamsProvider import updateLight

try:
    light = TrafficLight(DummySetter())
    while True:
        updateLight(light)
        time.sleep(30)

except KeyboardInterrupt:
    light.stop()
    print ("Goodbye.")
