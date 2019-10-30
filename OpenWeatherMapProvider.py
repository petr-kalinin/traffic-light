import time
import os
import json
import urllib.request
import graphyte
from logger import logger

APIKEY = os.environ["APIKEY"]

HOUR = 60 * 60
PERIOD_TO_ACCOUNT = 9 * HOUR
FORECAST_PERIOD_HOURS = 3

STATES = ((1e-2, True, False, False),
          (0.25, True, True, False),
          (0.8, False, True, False),
          (2, False, True, True),
          (1e20, False, False, True))

graphyte.init('ije.algoprog.ru', prefix='trfl')

def download_as_json(url):
    response = urllib.request.urlopen(url)
    text = response.read().decode('utf-8')
    return json.loads(text)


def calculate_flow(data):
    current_time = int(time.time())
    max_time = current_time + 9 * HOUR
    result = 0
    for forecast in data["list"]:
        if forecast["dt"] > max_time:
            break
        current = 0
        for tp, mult in ("rain", 1), ("snow", 3):
            if tp in forecast:
                print(tp, forecast[tp].get("3h", 0), mult)
                current += forecast[tp].get("3h", 0) * mult
        result = max(result, current)
    return result/FORECAST_PERIOD_HOURS


def update_light(traffic_light):
    try:
        url = "http://api.openweathermap.org/data/2.5/forecast?lat=56.326944&lon=44.0075&appid={}".format(APIKEY)
        data = download_as_json(url)
        flow = calculate_flow(data)
        logger.debug("flow={}".format(flow))
        graphyte.send("flow", flow)
        for i, state in enumerate(STATES):
            if flow <= state[0]:
                graphyte.send("state", i)
                traffic_light.set_constant(traffic_light.GREEN, state[1])
                traffic_light.set_constant(traffic_light.YELLOW, state[2])
                traffic_light.set_constant(traffic_light.RED, state[3])
                break
        else:
            raise Exception("Strange flow")
    except Exception as e:
        logger.error("error {}".format(e))
        traffic_light.set_constant(traffic_light.GREEN, False)
        traffic_light.set_constant(traffic_light.YELLOW, False)
        traffic_light.set_constant(traffic_light.RED, False)
