import time
import datetime
from logger import logger

class Updater:
    def __init__(self, other_provider):
        self._other_provider = other_provider

    def __call__(self, traffic_light):
        dow = datetime.datetime.today().weekday()
        start_time = 6 * 60 + 45
        end_time = 21 * 60 + 10
        if dow >= 5:
            start_time = 8 * 60
        t = time.localtime()
        current_time = t.tm_hour * 60 + t.tm_min
        logger.debug("current time: {}".format(current_time))
        if current_time < start_time or current_time > end_time:
            traffic_light.set_constant(traffic_light.GREEN, False)
            traffic_light.set_constant(traffic_light.YELLOW, False)
            traffic_light.set_constant(traffic_light.RED, False)
            return
        self._other_provider(traffic_light)

