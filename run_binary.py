#!/usr/bin/env python3
import time

from OrangePiSetter import OrangePiSetter
from TrafficLight import TrafficLight

try:
    light = TrafficLight(OrangePiSetter())
    i = 0
    while True:
        light.set_constant(light.RED, i % 2 == 1)
        light.set_constant(light.YELLOW, i // 2 % 2 == 1)
        light.set_constant(light.GREEN, i // 4 % 2 == 1)
        time.sleep(1)
        i += 1

except KeyboardInterrupt:
    light.stop()
    print ("Goodbye.")
