#!/usr/bin/env python3
import time

from DummySetter import DummySetter
from TrafficLight import TrafficLight

try:
    light = TrafficLight(DummySetter())
    light.set_periodic(light.RED, [2, 2])
    light.set_periodic(light.YELLOW, [4, 4])
    light.set_periodic(light.GREEN, [8, 8])

except KeyboardInterrupt:
    light.stop()
    print ("Goodbye.")
