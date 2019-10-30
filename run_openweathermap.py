#!/usr/bin/env python3
import time
import sys
from logger import logger

try:

    from TrafficLight import TrafficLight
    from OpenWeatherMapProvider import update_light
    from OffAtNightProviderAdapter import Updater
    from OffAtNightSetterAdapter import Setter as Adapter

    try:
        from OrangePiSetter import OrangePiSetter as Setter
    except:
        from DummySetter import DummySetter as Setter

    updater = update_light
    light = TrafficLight(Adapter(Setter()))
    while True:
        updater(light)
        time.sleep(60*10)

except BaseException as e:
    light.stop()
    logger.exception(e)
    logger.debug("Goodbye.")
