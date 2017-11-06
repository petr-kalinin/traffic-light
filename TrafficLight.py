import threading
import time


def constant(value):
    def generator(time):
        return value
    return generator


def periodic(timeouts, offset):
    values = []
    current = True
    for val in timeouts:
        values = values + [current] * val
        current = not current

    def generator(time):
        return values[(time + offset) % len(values)]
    return generator


class TrafficLight(object):
    RED = 0
    YELLOW = 1
    GREEN = 2

    def __init__(self, setter):
        self.generator = [constant(False)] * 3
        self.setter = setter
        self.generator_lock = threading.Lock()
        self.setter_thread = threading.Thread(target=self.set_light)
        self.stop_event = threading.Event()
        self.setter_thread.start()

    def stop(self):
        self.stop_event.set()

    def set_light(self):
        while not self.stop_event.is_set():
            with self.generator_lock:
                values = []
                for color in (self.RED, self.YELLOW, self.GREEN):
                    values.append(self.generator[color](int(time.time())))
            self.setter(*values)
            time.sleep(0.2)

    def set_generator(self, color, generator):
        with self.generator_lock:
            self.generator[color] = generator

    def set_constant(self, color, value):
        self.set_generator(color, constant(value))

    def set_periodic(self, color, timeouts, offset=None):
        self.set_generator(color, periodic(timeouts, offset or 0))
