import time

class Updater:
    def __init__(self, other_provider):
        self._other_provider = other_provider

    def __call__(self, traffic_light):
        START_TIME = 6 * 60 + 45
        END_TIME = 22 * 60
        t = time.localtime()
        current_time = t.tm_hour * 60 + t.tm_min
        print("current time: ", current_time)
        if current_time < START_TIME or current_time > END_TIME:
            traffic_light.set_constant(traffic_light.GREEN, False)
            traffic_light.set_constant(traffic_light.YELLOW, False)
            traffic_light.set_constant(traffic_light.RED, False)
            return
        self._other_provider(traffic_light)

