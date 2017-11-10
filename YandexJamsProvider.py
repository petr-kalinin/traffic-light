import time
import json
import urllib.request


def download_as_json(url):
    response = urllib.request.urlopen(url)
    text = response.read().decode('utf-8')
    return json.loads(text)


STATES = ((2, True, False, False),
          (4, True, True, False),
          (6, False, True, False),
          (8, False, True, True),
          (10, False, False, True))


def update_light(traffic_light):
    try:
        stamp_url = "https://api-maps.yandex.ru/services/coverage/v2/layers_stamps?lang=ru_RU&l=trf"
        stamp_data = download_as_json(stamp_url)
        stamp = stamp_data["trf"]["version"]
        print(stamp)
        url = 'https://jgo.maps.yandex.net/description/traffic-light?lang=ru_RU&ids=47&tm={}'.format(stamp)
        print(url)
        data = download_as_json(url)
        level = data["data"]["features"][0]["properties"]["JamsMetaData"]["level"]
        print("level=", level)
        for state in STATES:
            if level <= state[0]:
                traffic_light.set_constant(traffic_light.GREEN, state[1])
                traffic_light.set_constant(traffic_light.YELLOW, state[2])
                traffic_light.set_constant(traffic_light.RED, state[3])
                break
        else:
            raise Exception("Strange level")
    except Exception as e:
        print("error", e)
        traffic_light.set_constant(traffic_light.GREEN, False)
        traffic_light.set_periodic(traffic_light.YELLOW, [4, 4])
        traffic_light.set_constant(traffic_light.RED, False)



