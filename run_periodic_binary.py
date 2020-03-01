#!/usr/bin/python3.8 -u
import time

from OrangePiSetter import OrangePiSetter as Setter
from TrafficLight import TrafficLight

try:
    light = TrafficLight(Setter())
    light.set_periodic(light.RED, [2, 2])
    light.set_periodic(light.YELLOW, [4, 4])
    light.set_periodic(light.GREEN, [8, 8])

except KeyboardInterrupt:
    light.stop()
    print ("Goodbye.")
