import time
import datetime
from logger import logger

HOLIDAYS = (
    (1, 1),
    (2, 1),
    (3, 1),
    (4, 1),
    (5, 1),
    (6, 1),
    (7, 1),
    (8, 1),
    (23, 2),
    (24, 2),
    (8, 3),
    (9, 3),
    (10, 3),
    (1, 5),
    (2, 5),
    (3, 5),
    (4, 5),
    (5, 5),
    (9, 5),
    (10, 5),
    (11, 5),
    (12, 5),
    (12, 6),
    (2, 11),
    (3, 11),
    (4, 11))

class Updater:
    def __init__(self, other_provider):
        self._other_provider = other_provider

    def __call__(self, traffic_light):
        date = datetime.datetime.today()
        dow = date.weekday()
        day = date.day
        month = date.month
        start_time = 7 * 60
        end_time = 21 * 60 + 10
        if dow >= 5 or (day, month) in HOLIDAYS:
            start_time = 8 * 60 + 45
        t = time.localtime()
        current_time = t.tm_hour * 60 + t.tm_min
        logger.debug("current time: {}".format(current_time))
        if current_time < start_time or current_time > end_time:
            traffic_light.set_constant(traffic_light.GREEN, False)
            traffic_light.set_constant(traffic_light.YELLOW, False)
            traffic_light.set_constant(traffic_light.RED, False)
            return
        self._other_provider(traffic_light)

