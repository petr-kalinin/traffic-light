#!/usr/bin/env python3
import time

from DummySetter import DummySetter
from TrafficLight import TrafficLight
from YandexJamsProvider import update_light
from logger import logger

try:
    light = TrafficLight(DummySetter())
    while True:
        update_light(light)
        time.sleep(30)

except KeyboardInterrupt:
    light.stop()
    logger.debug("Goodbye.")
